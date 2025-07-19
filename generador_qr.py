import streamlit as st
import qrcode
from PIL import Image
import io

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Generador QR",
    page_icon="🔗",
    layout="centered"
)

# --- Función para Generar el QR ---
def generar_codigo_qr(data):
    """
    Genera una imagen de código QR a partir de los datos proporcionados.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta tolerancia a errores
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# --- Interfaz de la Aplicación ---

st.title("Generador de Códigos QR Sencillo 🔗")
st.write("Introduce una URL o el texto que quieras convertir en un código QR. El código se generará automáticamente.")

# 1. Campo de texto para la entrada del usuario
url_o_texto = st.text_input(
    "Introduce la URL o el texto aquí:",
    placeholder="Ej: https://www.streamlit.io"
)

# 2. Generar y mostrar el QR si hay texto en el campo
if url_o_texto:
    try:
        # Generar la imagen del QR
        imagen_qr = generar_codigo_qr(url_o_texto)

        st.image(imagen_qr, caption=f"Código QR para: '{url_o_texto}'", width=300)

        # Convertir la imagen a bytes para poder descargarla
        buf = io.BytesIO()
        imagen_qr.save(buf, format="PNG")
        bytes_imagen = buf.getvalue()

        # 3. Botón de descarga
        st.download_button(
            label="⬇️ Descargar Código QR (.png)",
            data=bytes_imagen,
            file_name="mi_codigo_qr.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"Ha ocurrido un error: {e}")

st.markdown("---")
st.write("Hecho con ❤️ usando Python y Streamlit.")
