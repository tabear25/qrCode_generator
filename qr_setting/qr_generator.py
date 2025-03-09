import qrcode

"""
以下のパラメーターを調整することで出力するQRコードの画像の余白サイズを修正可能
Parameters:
    - box_size: 1セル当たりのピクセル数（デフォルト: 10）
    - border: 境界のセル数（デフォルト: 4）
"""

def generate_qr_code(url, fill_color, back_color, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4):
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img
