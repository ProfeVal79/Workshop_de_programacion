from abc import ABC, abstractmethod
class InvoiceService(ABC):
 @abstractmethod
 def execute(self, invoice):
    pass
class InvoiceCalculator(InvoiceService):
 def execute(self, invoice):
    total = 0
    items = invoice.get('items', [])
    for item in items:
        subtotal_item = item ["precio"] * item["cantidad"]
        item["subtotal"] = subtotal_item
        total += subtotal_item
    invoice['total'] = total

class InvoiceDisplay(InvoiceService):
    def execute(self, invoice):
        print(f"Factura para {invoice['cliente']}")
        print("Items:")
        for item in invoice.get('items', []):
            print(f"{item['nombre']}: {item['cantidad']} Precio unitario: ${item['precio']} Subtotal: ${item['subtotal']}")
        print(f"Total:${invoice['total']}")

mi_factura = {"cliente": "Juan Pérez", "items": [{ "nombre": "producto1", "cantidad": 2, "precio": 10 }, { "nombre": "producto2", "cantidad": 1, "precio": 20 }]}
calculadora = InvoiceCalculator()
calculadora.execute(mi_factura)
mostrador = InvoiceDisplay()
mostrador.execute(mi_factura)