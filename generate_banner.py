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
    """Genera un banner ASCII con v31n73 y efectos dinámicos ultra llamativos"""
    
    # Obtener fecha y hora para efectos dinámicos
    now = datetime.datetime.now()
    hour = now.hour
    
    # Seleccionar tema de color basado en la hora
    if 6 <= hour < 12:  # Mañana - Amanecer
        gradient_colors = "from-yellow-400 via-orange-500 to-red-500"
        glow_color = "#FFD700"
        theme_emoji = "🌅"
    elif 12 <= hour < 18:  # Tarde - Energía
        gradient_colors = "from-blue-400 via-purple-500 to-pink-500"
        glow_color = "#00BFFF"
        theme_emoji = "⚡"
    elif 18 <= hour < 22:  # Noche - Creatividad
        gradient_colors = "from-purple-600 via-pink-600 to-blue-600"
        glow_color = "#9D4EDD"
        theme_emoji = "🌙"
    else:  # Madrugada - Misterio
        gradient_colors = "from-indigo-900 via-purple-900 to-pink-900"
        glow_color = "#4C1D95"
        theme_emoji = "🌌"
    
    # Banner ultra llamativo compatible con GitHub
    ascii_art = f"""<div align="center">

<!-- Banner principal con diseño llamativo -->
<table>
<tr>
<td align="center">

```
┌──────────────────────────────────────────────────────────────────────┐
│  {theme_emoji}  ██╗   ██╗██████╗  ██╗███╗   ██╗███████╗██████╗   {theme_emoji}  │
│     ██║   ██║╚════██╗███║████╗  ██║╚════██║╚════██╗     │
│     ██║   ██║ █████╔╝╚██║██╔██╗ ██║    ██╔╝ █████╔╝     │
│     ╚██╗ ██╔╝ ╚═══██╗ ██║██║╚██╗██║   ██╔╝  ╚═══██╗     │
│      ╚████╔╝ ██████╔╝ ██║██║ ╚████║   ██║   ██████╔╝      │
│       ╚═══╝  ╚═════╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═════╝       │
└──────────────────────────────────────────────────────────────────────┘
```

</td>
</tr>
</table>"""
    
    # Obtener fecha y hora actual
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Generar elementos dinámicos ultra llamativos
    coding_emojis = ["💻", "🚀", "⚡", "🔥", "✨", "🎯", "🎮", "🤖", "🎨", "🎵", "💡", "🌟", "🎆", "🔮", "✨", "🌌", "🌠"]
    random_emoji = random.choice(coding_emojis)
    
    # Emojis temáticos adicionales
    extra_emojis = ["🌈", "🎪", "🎭", "🎲", "🎸", "🎹", "🎤", "🎧", "🎆", "🎇", "✨", "🔮", "🌌"]
    extra_emoji = random.choice(extra_emojis)
    
    # Badges dinámicos y llamativos
    skill_badges = [
        f'<img src="https://img.shields.io/badge/Python-Expert-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>',
        f'<img src="https://img.shields.io/badge/JavaScript-Pro-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript"/>',
        f'<img src="https://img.shields.io/badge/AI-Enthusiast-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=tensorflow&logoColor=white" alt="AI"/>',
        f'<img src="https://img.shields.io/badge/Web_Dev-Master-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=react&logoColor=white" alt="Web Dev"/>'
    ]
    selected_badges = random.sample(skill_badges, 2)  # Seleccionar 2 badges aleatorios
    
    # Lenguajes de programación con badges llamativos
    color_hex = glow_color.replace('#', '')
    programming_languages = [
        f'<img src="https://img.shields.io/badge/Python-{color_hex}?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>',
        f'<img src="https://img.shields.io/badge/JavaScript-{color_hex}?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript"/>',
        f'<img src="https://img.shields.io/badge/Java-{color_hex}?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java"/>',
        f'<img src="https://img.shields.io/badge/C++-{color_hex}?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++"/>',
        f'<img src="https://img.shields.io/badge/HTML5-{color_hex}?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>',
        f'<img src="https://img.shields.io/badge/CSS3-{color_hex}?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>',
        f'<img src="https://img.shields.io/badge/React-{color_hex}?style=for-the-badge&logo=react&logoColor=white" alt="React"/>',
        f'<img src="https://img.shields.io/badge/Node.js-{color_hex}?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js"/>',
        f'<img src="https://img.shields.io/badge/Git-{color_hex}?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>',
        f'<img src="https://img.shields.io/badge/VS_Code-{color_hex}?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code"/>'
    ]
    
    # Citas inspiracionales ultra dinámicas
    quotes = [
        f"{theme_emoji} 'El código es poesía digital en movimiento'",
        f"{theme_emoji} 'Cada bug es una puerta hacia la perfección'",
        f"{theme_emoji} 'La creatividad no conoce límites en el universo digital'",
        f"{theme_emoji} 'Programar es esculpir el futuro con lógica'",
        f"{theme_emoji} 'El código elegante es arte en su forma más pura'",
        f"{theme_emoji} 'La innovación nace donde la curiosidad encuentra la lógica'",
        f"{theme_emoji} 'Cada algoritmo cuenta una historia épica'",
        f"{theme_emoji} 'El futuro se construye una línea de código a la vez'",
        f"{theme_emoji} 'Donde otros ven problemas, yo veo oportunidades de código'",
        f"{theme_emoji} 'La magia real sucede entre las llaves del código'"
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
    
    # Construir el banner ultra llamativo compatible con GitHub
    banner = f"""<div align="center">

{ascii_art}

<!-- Sección de título con emojis llamativos -->
<h1>
{random_emoji} <strong>DESARROLLADOR FULL STACK</strong> {random_emoji}<br>
{extra_emoji} <strong>CREADOR DIGITAL</strong> {extra_emoji}<br>
{theme_emoji} <strong>INNOVADOR TECNOLÓGICO</strong> {theme_emoji}
</h1>

<!-- Separador visual -->
<p>
{theme_emoji}────────────────────────────────────────────{theme_emoji}
</p>

<!-- Cita inspiracional destacada -->
<table>
<tr>
<td align="center">
<h2><em>{random_quote}</em></h2>
</td>
</tr>
</table>

<!-- Badges dinámicos en tabla -->
<table>
<tr>
<td align="center">
{selected_badges[0]}
</td>
<td align="center">
{selected_badges[1]}
</td>
</tr>
</table>

<!-- Estado actual destacado -->
<h3>
{random_emoji} <strong>ESTADO ACTUAL:</strong> <em>{status_text}</em> {random_emoji}
</h3>

<!-- Sección de lenguajes de programación -->
<h2>
💻 <strong>LENGUAJES & TECNOLOGÍAS</strong> 💻
</h2>

<!-- Separador para lenguajes -->
<p>
{theme_emoji}────────────────────────────────────────────{theme_emoji}
</p>

<!-- Lenguajes principales en tabla -->
<table>
<tr>
<td align="center">{programming_languages[0]}</td>
<td align="center">{programming_languages[1]}</td>
<td align="center">{programming_languages[2]}</td>
</tr>
<tr>
<td align="center">{programming_languages[3]}</td>
<td align="center">{programming_languages[4]}</td>
<td align="center">{programming_languages[5]}</td>
</tr>
<tr>
<td align="center">{programming_languages[6]}</td>
<td align="center">{programming_languages[7]}</td>
<td align="center">{programming_languages[8]}</td>
</tr>
</table>

<!-- Herramientas adicionales -->
<p align="center">
{programming_languages[9]}
</p>

<!-- Mensaje sobre lenguajes -->
<h4>
✨ <em>"Cada lenguaje es una nueva forma de pensar y crear"</em> ✨
</h4>

<!-- Sección de código destacada -->
<table>
<tr>
<td align="center">

```python
# 🚀 CLASE DUSTNACH - DESARROLLADOR DIGITAL 🚀
class DustNach:
    def __init__(self):
        self.name = "v31n73" 
        self.username = "DustNach" 
        self.role = "Full Stack Developer 🚀"
        self.languages = ["Python", "JavaScript", "Java", "C++", "HTML/CSS"]
        self.passion = ["AI 🤖", "Web Dev 🌐", "Game Dev 🎮", "Music Production 🎵"]
        self.current_focus = "Building amazing digital experiences ✨"
        self.status = "🔥 Siempre aprendiendo, siempre creando"
        self.power_level = "Over 9000! 💪"
    
    def say_hello(self):
        return "¡Hola! Bienvenido a mi universo digital 🌌👋"
    
    def get_current_project(self):
        projects = [
            "🎮 Desarrollando un juego indie revolucionario",
            "🤖 Creando un bot con IA avanzada", 
            "🎵 App de producción musical futurista",
            "💻 Plataforma web de próxima generación",
            "🚀 Herramientas de desarrollo innovadoras",
            "🌌 Sistema de realidad virtual inmersivo",
            "✨ Framework de desarrollo ultra rápido"
        ]
        import random
        return random.choice(projects)
    
    def coding_mood(self):
        moods = [
            "🎯 En modo creativo total",
            "🔥 Programando con pasión",
            "⚡ Energía de desarrollador al máximo",
            "🎆 Creando magia digital"
        ]
        import random
        return random.choice(moods)

# ✨ INSTANCIA DEL DESARROLLADOR ✨
dev = DustNach()
print(dev.say_hello())
print(f"Proyecto actual: {{dev.get_current_project()}}")
print(f"Mood: {{dev.coding_mood()}}")
print(f"Power Level: {{dev.power_level}}")
```

</td>
</tr>
</table>

<!-- Sección de estadísticas -->
<p align="center">
<img src="https://komarev.com/ghpvc/?username=DustNach&color={glow_color.replace('#', '')}&style=for-the-badge&label=Profile+Views" alt="Profile Views"/>
<img src="https://img.shields.io/badge/Status-Active-{glow_color.replace('#', '')}.svg?style=for-the-badge" alt="Status"/>
<img src="https://img.shields.io/badge/Mood-Creative-{glow_color.replace('#', '')}.svg?style=for-the-badge" alt="Mood"/>
</p>

<!-- Separador visual -->
<p align="center">
{theme_emoji}────────────────────────────────────────────{theme_emoji}
</p>

<!-- Timestamp destacado -->
<h4 align="center">
🕒 <strong>Última actualización:</strong> {timestamp}
</h4>

<!-- Mensaje final llamativo -->
<h2 align="center">
{theme_emoji} ¡GRACIAS POR VISITAR MI PERFIL DINÁMICO! {theme_emoji}
</h2>

<!-- Separador final -->
<p align="center">
{theme_emoji}{random_emoji}{extra_emoji}────────────────────────────────────{extra_emoji}{random_emoji}{theme_emoji}
</p>

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
