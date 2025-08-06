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
    
    # ASCII art mejorado con efectos visuales
    ascii_art = f"""<div align="center">

<!-- Efectos CSS para animaciones -->
<style>
@keyframes glow {{
  0%, 100% {{ text-shadow: 0 0 5px {glow_color}, 0 0 10px {glow_color}, 0 0 15px {glow_color}; }}
  50% {{ text-shadow: 0 0 10px {glow_color}, 0 0 20px {glow_color}, 0 0 30px {glow_color}; }}
}}
@keyframes float {{
  0%, 100% {{ transform: translateY(0px); }}
  50% {{ transform: translateY(-10px); }}
}}
@keyframes pulse {{
  0%, 100% {{ opacity: 1; }}
  50% {{ opacity: 0.7; }}
}}
.glow-text {{
  animation: glow 2s ease-in-out infinite;
  color: {glow_color};
  font-weight: bold;
}}
.float-animation {{
  animation: float 3s ease-in-out infinite;
}}
.pulse-animation {{
  animation: pulse 2s ease-in-out infinite;
}}
</style>

<!-- Banner principal con gradiente -->
<div class="float-animation" style="background: linear-gradient(45deg, #1a1a2e, #16213e, #0f3460); padding: 20px; border-radius: 15px; border: 2px solid {glow_color}; box-shadow: 0 0 20px {glow_color}40;">

<pre class="glow-text" style="font-size: 16px; line-height: 1.2;">
██╗   ██╗██████╗  ██╗███╗   ██╗███████╗██████╗ 
██║   ██║╚════██╗███║████╗  ██║╚════██║╚════██╗
██║   ██║ █████╔╝╚██║██╔██╗ ██║    ██╔╝ █████╔╝
╚██╗ ██╔╝ ╚═══██╗ ██║██║╚██╗██║   ██╔╝  ╚═══██╗
 ╚████╔╝ ██████╔╝ ██║██║ ╚████║   ██║   ██████╔╝
  ╚═══╝  ╚═════╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═════╝ 
</pre>

<!-- Línea decorativa animada -->
<div style="height: 3px; background: linear-gradient(90deg, transparent, {glow_color}, transparent); margin: 15px 0; border-radius: 2px; animation: pulse 1.5s ease-in-out infinite;"></div>

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
        f'<img src="https://img.shields.io/badge/Python-Expert-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>',
        f'<img src="https://img.shields.io/badge/JavaScript-Pro-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript"/>',
        f'<img src="https://img.shields.io/badge/AI-Enthusiast-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=tensorflow&logoColor=white" alt="AI"/>',
        f'<img src="https://img.shields.io/badge/Web_Dev-Master-{glow_color.replace("#", "")}.svg?style=for-the-badge&logo=react&logoColor=white" alt="Web Dev"/>'
    ]
    selected_badges = random.sample(skill_badges, 2)  # Seleccionar 2 badges aleatorios
    
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
    
    # Construir el banner ultra llamativo
    banner = f"""<div align="center">

{ascii_art}

<!-- Título principal con efectos -->
<h2 class="pulse-animation" style="background: linear-gradient(45deg, {glow_color}, #FF6B6B, #4ECDC4, #45B7D1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 24px; font-weight: bold; margin: 20px 0;">
{random_emoji} Desarrollador Full Stack | {extra_emoji} Creador Digital | {theme_emoji} Innovador
</h2>

<!-- Cita inspiracional con estilo -->
<div style="background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); backdrop-filter: blur(10px); border-radius: 10px; padding: 15px; margin: 20px 0; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
<h3 style="color: {glow_color}; margin: 0; font-style: italic;">{random_quote}</h3>
</div>

<!-- Badges dinámicos -->
<div style="margin: 20px 0;">
{' '.join(selected_badges)}
</div>

<!-- Estado actual con animación -->
<div class="float-animation" style="background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.2), rgba(255,255,255,0.1)); border-radius: 25px; padding: 10px 20px; margin: 15px 0; border: 2px solid {glow_color}; display: inline-block;">
<strong style="color: {glow_color};">{random_emoji} Estado actual:</strong> <em style="color: #FFD700;">{status_text}</em>
</div>

<!-- Sección de código con efectos -->
<div style="background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6)); border-radius: 15px; padding: 20px; margin: 20px 0; border: 1px solid {glow_color}; box-shadow: 0 0 20px rgba(0,0,0,0.5);">

```python
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
            "⚡ Energia de desarrollador al máximo",
            "🎆 Creando magia digital"
        ]
        import random
        return random.choice(moods)

# Instancia del desarrollador
dev = DustNach()
print(dev.say_hello())
print(f"Proyecto actual: {{dev.get_current_project()}}")
print(f"Mood: {{dev.coding_mood()}}")
print(f"Power Level: {{dev.power_level}}")
```

</div>

<!-- Sección de estadísticas con efectos -->
<div style="display: flex; justify-content: center; gap: 10px; margin: 20px 0; flex-wrap: wrap;">
<img src="https://komarev.com/ghpvc/?username=DustNach&color={glow_color.replace('#', '')}&style=for-the-badge&label=Profile+Views" alt="Profile Views" class="pulse-animation"/>
<img src="https://img.shields.io/badge/Status-Active-{glow_color.replace('#', '')}.svg?style=for-the-badge" alt="Status" class="float-animation"/>
<img src="https://img.shields.io/badge/Mood-Creative-{glow_color.replace('#', '')}.svg?style=for-the-badge" alt="Mood" class="pulse-animation"/>
</div>

<!-- Timestamp con efectos -->
<div style="background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); padding: 10px; border-radius: 10px; margin: 20px 0;">
<em style="color: {glow_color}; font-size: 14px;">🕒 Última actualización: {timestamp}</em>
</div>

<!-- Línea final decorativa -->
<div style="height: 2px; background: linear-gradient(90deg, transparent, {glow_color}, transparent); margin: 20px 0; border-radius: 1px;"></div>

<!-- Mensaje final -->
<div class="pulse-animation" style="margin: 15px 0;">
<h4 style="color: {glow_color}; margin: 0;">{theme_emoji} ¡Gracias por visitar mi perfil dinámico! {theme_emoji}</h4>
</div>

</div>

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
