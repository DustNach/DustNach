# 🚀 Perfil Dinámico de GitHub - DustNach

Este es un sistema automatizado que mantiene tu perfil de GitHub actualizado con contenido dinámico y un impresionante banner ASCII "v31n73".

## ✨ Características

- 🎯 **Banner ASCII "v31n73"** - Arte ASCII personalizado que se muestra prominentemente
- 🔄 **Actualización Automática** - Se ejecuta cada 4 horas via GitHub Actions
- 🎲 **Contenido Dinámico** - Emojis, citas y proyectos que cambian automáticamente
- 💻 **Código Python Interactivo** - Muestra tu perfil como una clase de Python
- 📊 **Estadísticas en Tiempo Real** - Contador de visitas y timestamps
- 🎮 **Elementos Lúdicos** - Combina profesionalismo con diversión

## 🛠️ Configuración Automática

### 1. ¡Ya está listo!
Este repositorio ya está configurado y funcionando. Solo necesitas:

1. **Hacer push a GitHub**:
   ```bash
   git add .
   git commit -m "🚀 Initial dynamic profile setup"
   git push origin main
   ```

2. **Habilitar GitHub Actions**:
   - Ve a tu repositorio en GitHub
   - Settings → Actions → General
   - Selecciona "Allow all actions and reusable workflows"
   - En "Workflow permissions", marca "Read and write permissions"

### 2. Ejecución Manual (Opcional)
```bash
python generate_banner.py
```

## 📁 Estructura del Proyecto

```
DustNach/
├── README.md                    # Tu perfil principal (se actualiza automáticamente)
├── generate_banner.py          # Generador del banner dinámico
├── requirements.txt            # Dependencias (ninguna externa requerida)
├── SETUP.md                   # Esta documentación
└── .github/
    └── workflows/
        └── update-banner.yml   # Automatización cada 4 horas
```

## 🎨 Personalización

### Cambiar Citas
Edita la lista `quotes` en `generate_banner.py`:
```python
quotes = [
    "💡 'Tu cita personalizada aquí'",
    "🚀 'Otra cita inspiradora'",
    # Agrega más...
]
```

### Modificar Proyectos
Actualiza la función `get_current_project()`:
```python
projects = [
    "🎮 Tu proyecto actual",
    "🤖 Otra idea genial",
    # Agrega más...
]
```

### Cambiar Frecuencia
En `.github/workflows/update-banner.yml`:
```yaml
- cron: '0 */4 * * *'  # Cada 4 horas
- cron: '0 */2 * * *'  # Cada 2 horas
- cron: '0 */1 * * *'  # Cada hora
```

## 🎯 Elementos Dinámicos

- **ASCII Art**: "v31n73" en arte ASCII impresionante
- **Emojis Rotativos**: Cambian en cada actualización
- **Citas Inspiradoras**: Frases motivacionales aleatorias
- **Timestamp**: Muestra cuándo se actualizó por última vez
- **Código Python**: Tu perfil representado como una clase
- **Contador de Visitas**: Tracking automático de visualizaciones

## 🚀 ¡Funcionamiento Automático!

Una vez que hagas push a GitHub:
1. ✅ El banner se generará automáticamente
2. 🔄 Se actualizará cada 4 horas
3. 🎯 Contenido fresco siempre
4. 📊 Estadísticas en tiempo real

## 🎮 Diversión + Profesionalismo

Este perfil combina:
- 💼 **Profesional**: Muestra tus habilidades y proyectos
- 🎮 **Lúdico**: ASCII art, emojis y elementos divertidos
- 🤖 **Técnico**: Código Python real y funcional
- ✨ **Único**: Contenido que cambia constantemente

¡Disfruta de tu perfil dinámico único! 🎉
