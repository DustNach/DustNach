#!/usr/bin/env python3
"""
Script para generar un banner animado con 'v31n73' en ASCII art
"""

import datetime
import random

def generate_v31n73_banner():
    """Genera un banner ASCII con v31n73 y efectos dinámicos"""
    
    # ASCII art para v31n73
    ascii_art = """
██╗   ██╗██████╗  ██╗███╗   ██╗███████╗██████╗ 
██║   ██║╚════██╗███║████╗  ██║╚════██║╚════██╗
██║   ██║ █████╔╝╚██║██╔██╗ ██║    ██╔╝ █████╔╝
╚██╗ ██╔╝ ╚═══██╗ ██║██║╚██╗██║   ██╔╝  ╚═══██╗
 ╚████╔╝ ██████╔╝ ██║██║ ╚████║   ██║   ██████╔╝
  ╚═══╝  ╚═════╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═════╝ 
"""
    
    # Obtener fecha y hora actual
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Generar elementos dinámicos
    coding_emojis = ["💻", "🚀", "⚡", "🔥", "✨", "🎯", "🎮", "🤖"]
    random_emoji = random.choice(coding_emojis)
    
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
    
    banner = f"""
<div align="center">

{ascii_art}

### 🎯 Desarrollador Full Stack | {random_emoji} Creador Digital | 🚀 Innovador

{random_quote}

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

</div>
"""
    
    return banner

def update_readme():
    """Actualiza el README.md con el nuevo banner"""
    banner = generate_v31n73_banner()
    
    # Leer el README actual
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = ""
    
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
    else:
        # Agregar banner al inicio
        new_content = f"{banner_start}\n{banner}\n{banner_end}\n\n{content}"
    
    # Escribir el nuevo contenido
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ Banner actualizado exitosamente!")

if __name__ == "__main__":
    update_readme()
