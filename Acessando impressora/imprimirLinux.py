
import cups

conn = cups.Connection()
# printers = conn.getPrinters()
printer_name = 'printer'  # Choose the printer you want to use

file_name = "output_image613x953.jpg"  # Path to the image file you want to print

print_job_options = {
    "media": "A4",  # Specify the media size (e.g., A4, Letter)
    "print-scaling": "fill"
    # "fitplot": "True"  # Scale the image to fit the page
}

job_id = conn.printFile(printer_name, file_name, "Python Print Job", print_job_options)
print("Print job ID:", job_id)
