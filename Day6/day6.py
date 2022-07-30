# Create QRcode
import qrcode
import cv2

msg = qrcode.make("Happy Friendship day, Buddies")
msg.save("Greetings.jpg")

# Decode QRcode
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("suspiciousMs.jpg"))
print(val)