"""
Script para descargar índice FAISS desde GitHub Release
Se ejecuta automáticamente al iniciar la app en Streamlit Cloud
"""
import os
import requests
import streamlit as st

def download_faiss_from_release():
    """
    Descarga el índice FAISS desde GitHub Release si no existe localmente.
    Retorna True si el índice está disponible (ya existía o se descargó).
    """
    REPO = "arguellosolanogerardo-cloud/consultor-gerard-v3"
    TAG = "faiss-index-v1"
    
    # Verificar si ya existe
    if os.path.exists("faiss_index/index.faiss") and os.path.exists("faiss_index/index.pkl"):
        print("[INFO] Índice FAISS ya existe localmente")
        return True
    
    print("[INFO] Índice FAISS no encontrado, descargando desde GitHub Release...")
    
    # Crear directorio
    os.makedirs("faiss_index", exist_ok=True)
    
    # URLs de descarga
    files = {
        "index.faiss": f"https://github.com/{REPO}/releases/download/{TAG}/index.faiss",
        "index.pkl": f"https://github.com/{REPO}/releases/download/{TAG}/index.pkl"
    }
    
    try:
        for filename, url in files.items():
            filepath = f"faiss_index/{filename}"
            
            print(f"[INFO] Descargando {filename}...")
            
            # Mostrar progreso en Streamlit si está disponible
            try:
                with st.spinner(f"📥 Descargando {filename}..."):
                    response = requests.get(url, stream=True)
                    response.raise_for_status()
                    
                    total_size = int(response.headers.get('content-length', 0))
                    downloaded = 0
                    
                    with open(filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                    
                    print(f"[INFO] {filename} descargado exitosamente ({downloaded/(1024*1024):.1f} MB)")
                    
            except:
                # Si Streamlit no está disponible (modo local), descargar sin spinner
                response = requests.get(url, stream=True)
                response.raise_for_status()
                
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                print(f"[INFO] {filename} descargado exitosamente")
        
        # Crear marcador de descarga completa
        with open("faiss_index/.faiss_ready", "w") as f:
            f.write("downloaded")
        
        print("[INFO] ✅ Índice FAISS descargado completamente")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error descargando índice FAISS: {e}")
        return False

if __name__ == "__main__":
    # Para testing local
    success = download_faiss_from_release()
    if success:
        print("✅ Índice FAISS listo para usar")
    else:
        print("❌ Error descargando índice FAISS")
