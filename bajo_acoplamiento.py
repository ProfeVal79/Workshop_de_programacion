class InvoiceCalculator:
 def calculate_total(self, invoice):
    total = 0
    items = invoice.get('items', [])
    for item in items:
        subtotal_item = item ["precio"] * item["cantidad"]
        item["subtotal"] = subtotal_item
        total += subtotal_item
    invoice['total'] = total

class InvoiceDisplay:
    def display_invoice(self, invoice):
        print(f"Factura para {invoice['cliente']}")
        print("Items:")
        for item in invoice.get('items', []):
            print(f"{item['nombre']}: {item['cantidad']} Precio unitario: ${item['precio']} Subtotal: ${item['subtotal']}")
        print(f"Total:${invoice['total']}")

mi_factura = {"cliente": "Juan Pérez", "items": [{ "nombre": "producto1", "cantidad": 2, "precio": 10 }, { "nombre": "producto2", "cantidad": 1, "precio": 20 }]}
calculadora = InvoiceCalculator()
calculadora.calculate_total(mi_factura)
mostrador = InvoiceDisplay()
mostrador.display_invoice(mi_factura)