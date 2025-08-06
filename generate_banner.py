#!/usr/bin/env python3
"""
Script para generar un banner animado con 'v31n73' en ASCII art
Con manejo robusto de errores y logging
"""

import datetime
import random
import sys
import os

# Configurar codificación UTF-8 para Windows
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

def generate_v31n73_banner():
    """Genera un banner ASCII con v31n73 y efectos dinámicos"""
    
    # ASCII art para v31n73 - Mejorado para GitHub
    ascii_art = """<pre>
██╗   ██╗██████╗  ██╗███╗   ██╗███████╗██████╗ 
██║   ██║╚════██╗███║████╗  ██║╚════██║╚════██╗
██║   ██║ █████╔╝╚██║██╔██╗ ██║    ██╔╝ █████╔╝
╚██╗ ██╔╝ ╚═══██╗ ██║██║╚██╗██║   ██╔╝  ╚═══██╗
 ╚████╔╝ ██████╔╝ ██║██║ ╚████║   ██║   ██████╔╝
  ╚═══╝  ╚═════╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═════╝ 
</pre>"""
    
    # Obtener fecha y hora actual
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Generar elementos dinámicos más variados
    coding_emojis = ["💻", "🚀", "⚡", "🔥", "✨", "🎯", "🎮", "🤖", "🎨", "🎵", "💡", "🌟"]
    random_emoji = random.choice(coding_emojis)
    
    # Emoji adicional para más variación
    extra_emojis = ["🌈", "🎪", "🎭", "🎲", "🎸", "🎹", "🎤", "🎧"]
    extra_emoji = random.choice(extra_emojis)
    
    # Citas de programación dinámicas
    quotes = [
        "💡 'El código es poesía en movimiento'",
        "🚀 'Cada bug es una oportunidad de aprender'",
        "⚡ 'La creatividad no tiene límites en el código'",
        "🎯 'Programar es resolver problemas con estilo'",
        "🔥 'El mejor código es el que otros pueden entender'",
        "✨ 'La innovación nace de la curiosidad'",
        "🎮 'Cada línea de código cuenta una historia'",
        "🤖 'El futuro se construye con código'"
    ]
    random_quote = random.choice(quotes)
    
    # Estado dinámico basado en la hora
    hour = now.hour
    if 6 <= hour < 12:
        status_emoji = "☕"
        status_text = "Modo café matutino activado"
    elif 12 <= hour < 18:
        status_emoji = "🚀"
        status_text = "Productividad al máximo"
    elif 18 <= hour < 22:
        status_emoji = "🎮"
        status_text = "Hora de crear y experimentar"
    else:
        status_emoji = "🌙"
        status_text = "Programando bajo las estrellas"
    
    # Crear el banner completo
    banner = f"""<div align="center">

{ascii_art}

### 🎯 Desarrollador Full Stack | {random_emoji} Creador Digital | {extra_emoji} Innovador

{random_quote}

**{status_emoji} Estado actual:** *{status_text}*

```python
class DustNach:
    def __init__(self):
        self.name = "v31n73"
        self.username = "DustNach"
        self.role = "Full Stack Developer"
        self.languages = ["Python", "JavaScript", "Java", "C++", "HTML/CSS"]
        self.passion = ["AI", "Web Dev", "Game Dev", "Music Production"]
        self.current_focus = "Building amazing digital experiences"
        self.status = "🔥 Siempre aprendiendo, siempre creando"
    
    def say_hello(self):
        return "¡Hola! Bienvenido a mi perfil de GitHub 👋"
    
    def get_current_project(self):
        projects = [
            "🎮 Desarrollando un juego indie",
            "🤖 Creando un bot inteligente", 
            "🎵 App de producción musical",
            "💻 Plataforma web innovadora",
            "🚀 Herramientas de desarrollo"
        ]
        import random
        return random.choice(projects)
    
    def coding_mood(self):
        return "🎯 En modo creativo total"

# Instancia del desarrollador
dev = DustNach()
print(dev.say_hello())
print(f"Proyecto actual: {{dev.get_current_project()}}")
print(f"Estado: {{dev.status}}")
```

<img src="https://komarev.com/ghpvc/?username=DustNach&color=blueviolet&style=flat-square&label=Profile+Views" alt="Profile Views"/>

*🕒 Última actualización: {timestamp}*

---

</div>"""
    
    return banner

def update_readme():
    """Actualiza el README.md con el nuevo banner con manejo robusto de errores"""
    try:
        print("🔄 Generando nuevo banner...")
        banner = generate_v31n73_banner()
        
        if not banner or len(banner.strip()) == 0:
            raise ValueError("Banner generado está vacío")
        
        # Leer el README actual
        readme_path = 'README.md'
        content = ""
        
        if os.path.exists(readme_path):
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"📖 README existente leído ({len(content)} caracteres)")
            except Exception as e:
                print(f"⚠️ Error leyendo README existente: {e}")
                content = ""
        else:
            print("📝 Creando nuevo README.md")
        
        # Buscar y reemplazar el banner existente o agregarlo al inicio
        banner_start = "<!-- BANNER_START -->"
        banner_end = "<!-- BANNER_END -->"
        
        if banner_start in content and banner_end in content:
            # Reemplazar banner existente
            start_idx = content.find(banner_start)
            end_idx = content.find(banner_end) + len(banner_end)
            new_content = (content[:start_idx] + 
                          f"{banner_start}\n{banner}\n{banner_end}" + 
                          content[end_idx:])
            print("🔄 Banner existente reemplazado")
        else:
            # Agregar banner al inicio
            new_content = f"{banner_start}\n{banner}\n{banner_end}\n\n{content}"
            print("➕ Banner agregado al inicio del README")
        
        # Validar que el contenido no esté vacío
        if not new_content or len(new_content.strip()) == 0:
            raise ValueError("Contenido final del README está vacío")
        
        # Crear backup del README anterior si existe
        if os.path.exists(readme_path) and len(content) > 0:
            backup_path = f"README.md.backup.{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
            try:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"💾 Backup creado: {backup_path}")
            except Exception as e:
                print(f"⚠️ No se pudo crear backup: {e}")
        
        # Escribir el nuevo contenido
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Banner actualizado exitosamente! ({len(new_content)} caracteres)")
        print(f"🕒 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error actualizando README: {e}")
        print(f"🔍 Detalles del error: {type(e).__name__}")
        return False

if __name__ == "__main__":
    try:
        success = update_readme()
        if success:
            print("🎉 Proceso completado exitosamente!")
            sys.exit(0)
        else:
            print("💥 Proceso falló")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️ Proceso interrumpido por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Error crítico: {e}")
        sys.exit(1)
