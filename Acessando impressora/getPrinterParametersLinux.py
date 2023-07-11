import cups

conn = cups.Connection()
printers = conn.getPrinters()

# for printer in printers:
#     print(printer)
printer_name = 'printer_name'  # Choose the printer you want to use

print_job_options = conn.getPrinterAttributes(printer_name)["media-supported"]


print("Available print job options:")
for option in print_job_options:
    print(option)

# printer_attributes = conn.getPrinterAttributes(printer_name)

# print("Printer attributes for", printer_name + ":")
# for key, value in printer_attributes.items():
#     print(key + ":", value)
#     print('####')