from llama_index.readers.file import PDFReader
from typing import Union, List, Literal
import glob
from tqdm import tqdm
import multiprocessing
import os

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
pdf_dir = "../../data_source"

class PDFLoader():
  def __init__(self, pdf_files: Union[str, List[str]]):
    """
    Khởi tạo PDFLoader với danh sách file PDF.
    """

    self.pdf_files = pdf_files

  @staticmethod
  def remove_non_utf8_characters(text: str) -> str:
    """
    Loại bỏ các ký tự không phải ASCII (dùng ord(char) < 128).
    """
    return ''.join(char for char in text if ord(char) < 128)

  def load_pdf(self, pdf_file: str) -> str:
    """
    Load một file PDF sử dụng PDFReader của llama_index.

    :param pdf_file: Đường dẫn file PDF
    :return: Danh sách document được load từ file PDF.
    """
    try:
      loader = PDFReader()
      documents = loader.load_data(pdf_file)

    except Exception as e:
      print(f"Lỗi khi load {pdf_file}: {e}")
      documents = []
    return documents

  def __call__(self, workers: int = 4) -> List:
    """
    Sử dụng multiprocessing để load song song nhiều file PDF.

    :param workers: Số lượng worker/processes sử dụng.
    :return: Danh sách các document được load.
    """
    num_processes = min(multiprocessing.cpu_count(), workers)
    docs_loaded = []
    total_files = len(self.pdf_files)

    with multiprocessing.Pool(processes=num_processes) as pool:
      with tqdm(total=total_files, desc="Loading PDFs", unit="file") as pbar:
        for result in pool.imap_unordered(self.load_pdf, self.pdf_files):
          docs_loaded.extend(result)
          pbar.update(1)

    return docs_loaded

class Loader:
  def __init__(self, pdf_dir: str, workers: int = 4):
    self.pdf_dir = pdf_dir
    self.workers = workers
    self.pdf_files = self._get_pdf_files()
    self.documents = self._load_documents()

  def _get_pdf_files(self):
    pdf_files = [
        os.path.join(self.pdf_dir, f)
        for f in os.listdir(self.pdf_dir)
        if f.endswith(".pdf")
    ]
    if not pdf_files:
      print(f"❌ Không tìm thấy file PDF trong thư mục: {self.pdf_dir}")
    else:
      print(f"📄 Tìm thấy {len(pdf_files)} file PDF.")
    return pdf_files

  def _load_documents(self):
    if not self.pdf_files:
      return None
    doc_loader = PDFLoader(self.pdf_files)
    documents = doc_loader(workers=self.workers)
    print(
        f"✅ Đã load {len(documents)} documents từ {len(self.pdf_files)} file PDF.")
    return documents

  def get_documents(self):
    return self.documents
