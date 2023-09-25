#noqa
"""We load the OCR engines here by default"""
from app.controllers.OCR import azure, local
from app.core.config import cfg
from app.controllers import paddleocr
global G_OCR 
G_OCR = {
    "azure_layout": azure.AzureLayoutOCR(cfg = cfg),
    "pytesseract": local.pyTesseractOCR(cfg = cfg),
    "azure_invoice": azure.AzureInvoiceOCR(cfg = cfg)
}

