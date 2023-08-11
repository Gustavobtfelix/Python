import cups

conn = cups.Connection()
printers = conn.getPrinters()

print(printers)

for printer in printers:
    print(printer, printers[printer]["keys"])
