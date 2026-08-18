import qrcode

upi_id = input("Enter your UPI ID: ")

upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=12324"

qr = qrcode.make(upi_url)

#qr.save("upi_qr.png")
qr.show()