import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
user_data=input("Enter the link or an url which should be turned into qrcode")
qr.add_data(user_data)
qr.make(fit=True)
try:
    a=input("Enter the background color of qr code").lower().strip()
    b=input("Enter the color of qr code").lower().strip()
except Exception:
    print("Sorry,Color can't be produced ,please try any another colors")    
img = qr.make_image(fill_color=b, back_color=a)
img.save("new.png")
type(img)