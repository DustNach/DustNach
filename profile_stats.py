#!/usr/bin/env python3
"""
Generador de estadísticas avanzadas para el perfil
"""

import random
import datetime

def get_coding_stats():
    """Genera estadísticas de programación dinámicas"""
    stats = {
        "lines_coded_today": random.randint(50, 500),
        "commits_this_week": random.randint(5, 25),
        "projects_active": random.randint(2, 8),
        "coffee_cups": random.randint(1, 6),
        "bugs_fixed": random.randint(3, 15)
    }
    return stats

def get_mood_emoji():
    """Retorna un emoji basado en la hora del día"""
    hour = datetime.datetime.now().hour
    
    if 5 <= hour < 9:
        return "☕"  # Café matutino
    elif 9 <= hour < 12:
        return "💻"  # Productivo
    elif 12 <= hour < 14:
        return "🍕"  # Almuerzo
    elif 14 <= hour < 18:
        return "🚀"  # Tarde productiva
    elif 18 <= hour < 22:
        return "🎮"  # Tiempo de relajación
    else:
        return "🌙"  # Noche de código

def generate_tech_stack():
    """Genera una representación visual del stack tecnológico"""
    return """
## 🛠️ Mi Stack Tecnológico

```
Frontend    ████████████░░  85%
Backend     ██████████░░░░  75%
Mobile      ████████░░░░░░  60%
DevOps      ██████░░░░░░░░  45%
AI/ML       ████████░░░░░░  65%
```
"""

def get_random_project_idea():
    """Genera ideas de proyectos aleatorias"""
    ideas = [
        "🎵 Sintetizador virtual con IA",
        "🎮 Juego de puzzles minimalista",
        "🤖 Chatbot para desarrolladores",
        "📱 App de productividad gamificada",
        "🎨 Generador de arte procedural",
        "🚀 Herramienta de deployment automático",
        "📊 Dashboard de métricas personales"
    ]
    return random.choice(ideas)

if __name__ == "__main__":
    stats = get_coding_stats()
    print("📊 Estadísticas del día:")
    print(f"  • Líneas de código: {stats['lines_coded_today']}")
    print(f"  • Commits esta semana: {stats['commits_this_week']}")
    print(f"  • Proyectos activos: {stats['projects_active']}")
    print(f"  • Tazas de café: {stats['coffee_cups']}")
    print(f"  • Bugs arreglados: {stats['bugs_fixed']}")
    print(f"\n🎯 Estado actual: {get_mood_emoji()}")
    print(f"💡 Próxima idea: {get_random_project_idea()}")
    print(generate_tech_stack())
