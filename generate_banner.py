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
    
    # Seleccionar tema masculino basado en la hora
    if 6 <= hour < 12:  # Mañana - Profesional
        primary_color = "#1e3a8a"  # Azul oscuro profesional
        secondary_color = "#1f2937"  # Gris oscuro
        accent_color = "#3b82f6"  # Azul brillante
        theme_emoji = "⚙️"  # Engranaje
        theme_name = "PROFESSIONAL"
    elif 12 <= hour < 18:  # Tarde - Tecnológico
        primary_color = "#0f172a"  # Negro azulado
        secondary_color = "#334155"  # Gris azulado
        accent_color = "#06b6d4"  # Cian tecnológico
        theme_emoji = "🔧"  # Llave inglesa
        theme_name = "TECH"
    elif 18 <= hour < 22:  # Noche - Elegante
        primary_color = "#111827"  # Negro elegante
        secondary_color = "#374151"  # Gris medio
        accent_color = "#10b981"  # Verde esmeralda
        theme_emoji = "🎯"  # Diana
        theme_name = "ELITE"
    else:  # Madrugada - Misterioso
        primary_color = "#0c0a09"  # Negro profundo
        secondary_color = "#292524"  # Marrón oscuro
        accent_color = "#f59e0b"  # Dorado
        theme_emoji = "⚡"  # Rayo
        theme_name = "STEALTH"
    
    # Banner masculino perfectamente organizado
    ascii_art = f"""<div align="center">

<!-- Header con tema dinámico -->
<img src="https://capsule-render.vercel.app/api?type=waving&color={accent_color.replace('#', '')}&height=120&section=header&text=MODE:%20{theme_name}&fontSize=24&fontColor=ffffff&animation=fadeIn" alt="Header"/>

<br>

<!-- Banner principal con diseño masculino perfectamente centrado -->
<table align="center" width="100%">
<tr>
<td align="center">

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                    ┃
┃  {theme_emoji}  ██╗   ██╗██████╗  ██╗███╗   ██╗███████╗██████╗   {theme_emoji}  ┃
┃     ██║   ██║╚════██╗███║████╗  ██║╚════██║╚════██╗     ┃
┃     ██║   ██║ █████╔╝╚██║██╔██╗ ██║    ██╔╝ █████╔╝     ┃
┃     ╚██╗ ██╔╝ ╚═══██╗ ██║██║╚██╗██║   ██╔╝  ╚═══██╗     ┃
┃      ╚████╔╝ ██████╔╝ ██║██║ ╚████║   ██║   ██████╔╝      ┃
┃       ╚═══╝  ╚═════╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═════╝       ┃
┃                                                                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

</td>
</tr>
</table>

<br>

<!-- Efecto visual con typing SVG centrado -->
<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&weight=900&size=32&duration=3000&pause=1000&color={accent_color.replace('#', '')}&center=true&vCenter=true&multiline=true&width=700&height=120&lines=FULL+STACK+DEVELOPER;DIGITAL+CREATOR;TECH+INNOVATOR" alt="Typing SVG" />
</div>"""
    
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
        f'<img src="https://img.shields.io/badge/Python-Expert-{accent_color.replace("#", "")}.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>',
        f'<img src="https://img.shields.io/badge/JavaScript-Pro-{accent_color.replace("#", "")}.svg?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript"/>',
        f'<img src="https://img.shields.io/badge/AI-Enthusiast-{accent_color.replace("#", "")}.svg?style=for-the-badge&logo=tensorflow&logoColor=white" alt="AI"/>',
        f'<img src="https://img.shields.io/badge/Web_Dev-Master-{accent_color.replace("#", "")}.svg?style=for-the-badge&logo=react&logoColor=white" alt="Web Dev"/>'
    ]
    selected_badges = random.sample(skill_badges, 2)  # Seleccionar 2 badges aleatorios
    
    # Lenguajes de programación con badges llamativos
    color_hex = accent_color.replace('#', '')
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

<!-- Separador con efecto -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=6" alt="Divider"/>

<br>

<!-- Panel de estado profesional perfectamente alineado -->
<table align="center" width="90%" cellpadding="10" cellspacing="0">
<tr>
<td align="center" width="33.33%">
    <img src="https://img.shields.io/badge/STATUS-{status_text.replace(' ', '%20')}-{accent_color.replace('#', '')}?style=for-the-badge&logo=statuspage&logoColor=white" alt="Status"/>
</td>
<td align="center" width="33.33%">
    <img src="https://img.shields.io/badge/MODE-{theme_name}-{primary_color.replace('#', '')}?style=for-the-badge&logo=atom&logoColor=white" alt="Mode"/>
</td>
<td align="center" width="33.33%">
    <img src="https://img.shields.io/badge/LEVEL-EXPERT-{accent_color.replace('#', '')}?style=for-the-badge&logo=starship&logoColor=white" alt="Level"/>
</td>
</tr>
</table>

<br>

<!-- Estadísticas principales perfectamente centradas -->
<table align="center" width="100%" cellpadding="10" cellspacing="0">
<tr>
<td align="center" width="50%">
    <img src="https://github-readme-stats.vercel.app/api?username=DustNach&show_icons=true&theme=dark&bg_color={primary_color.replace('#', '')}&title_color={accent_color.replace('#', '')}&icon_color={accent_color.replace('#', '')}&text_color=ffffff&border_color={secondary_color.replace('#', '')}" alt="GitHub Stats" height="180" width="400"/>
</td>
<td align="center" width="50%">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=DustNach&layout=compact&theme=dark&bg_color={primary_color.replace('#', '')}&title_color={accent_color.replace('#', '')}&text_color=ffffff&border_color={secondary_color.replace('#', '')}" alt="Top Languages" height="180" width="400"/>
</td>
</tr>
</table>

<br>

<!-- Contador de visitas centrado -->
<div align="center">
    <img src="https://komarev.com/ghpvc/?username=DustNach&label=PROFILE%20VIEWS&color={accent_color.replace('#', '')}&style=for-the-badge" alt="Profile views" />
</div>

<!-- Cita inspiracional destacada -->
<table align="center">
<tr>
<td align="center">
<h3><em>{random_quote}</em></h3>
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

<br>

<!-- Separador con efecto para lenguajes -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=6" alt="Divider"/>

<br>

<!-- Sección de lenguajes perfectamente organizada -->
<div align="center">
<h2>💻 <strong>LENGUAJES & TECNOLOGÍAS</strong> 💻</h2>
</div>

<br>

<!-- Lenguajes principales en tabla perfectamente alineada -->
<table align="center" width="90%" cellpadding="15" cellspacing="0">
<tr>
<td align="center" width="33.33%">{programming_languages[0]}</td>
<td align="center" width="33.33%">{programming_languages[1]}</td>
<td align="center" width="33.33%">{programming_languages[2]}</td>
</tr>
<tr>
<td align="center" width="33.33%">{programming_languages[3]}</td>
<td align="center" width="33.33%">{programming_languages[4]}</td>
<td align="center" width="33.33%">{programming_languages[5]}</td>
</tr>
<tr>
<td align="center" width="33.33%">{programming_languages[6]}</td>
<td align="center" width="33.33%">{programming_languages[7]}</td>
<td align="center" width="33.33%">{programming_languages[8]}</td>
</tr>
</table>

<br>

<!-- Herramientas adicionales centradas -->
<div align="center">
<h4>🛠️ <strong>HERRAMIENTAS:</strong> {programming_languages[9]}</h4>
</div>

<!-- Mensaje sobre lenguajes -->
<h4>
✨ <em>"Cada lenguaje es una nueva forma de pensar y crear"</em> ✨
</h4>

<br>

<!-- Separador con efecto para código -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=6" alt="Divider"/>

<br>

<!-- Sección de código perfectamente centrada -->
<table align="center" width="95%" cellpadding="20" cellspacing="0">
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

<br>

<!-- Footer masculino con efectos visuales -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=8" alt="Divider"/>

<br>

<!-- Timestamp con estilo centrado -->
<div align="center">
    <img src="https://img.shields.io/badge/LAST%20UPDATE-{timestamp.replace(' ', '%20').replace(':', '%3A')}-{accent_color.replace('#', '')}?style=for-the-badge&logo=clockify&logoColor=white" alt="Last Update"/>
</div>

<br>

<!-- Footer con wave effect -->
<img src="https://capsule-render.vercel.app/api?type=waving&color={accent_color.replace('#', '')}&height=120&section=footer&text=THANKS%20FOR%20VISITING&fontSize=24&fontColor=ffffff&animation=fadeIn" alt="Footer"/>
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
