#!/usr/bin/env python3
"""
Script para probar el flujo de trabajo localmente
Simula lo que hace GitHub Actions
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Ejecuta un comando y muestra el resultado"""
    print(f"\n🔄 {description}")
    print(f"💻 Ejecutando: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - EXITOSO")
            if result.stdout:
                print(f"📤 Salida: {result.stdout.strip()}")
        else:
            print(f"❌ {description} - FALLÓ")
            if result.stderr:
                print(f"🚨 Error: {result.stderr.strip()}")
        return result.returncode == 0
    except Exception as e:
        print(f"💥 Error ejecutando comando: {e}")
        return False

def main():
    """Simula el flujo de GitHub Actions localmente"""
    print("🚀 PRUEBA LOCAL DEL FLUJO DE GITHUB ACTIONS")
    print("=" * 50)
    
    # Paso 1: Validar sintaxis Python
    success = run_command(
        "python -m py_compile generate_banner.py",
        "Validando sintaxis del script Python"
    )
    if not success:
        print("💥 Fallo en validación de sintaxis")
        return False
    
    # Paso 2: Generar banner
    success = run_command(
        "python generate_banner.py",
        "Generando nuevo banner dinámico"
    )
    if not success:
        print("💥 Fallo generando banner")
        return False
    
    # Paso 3: Verificar cambios
    success = run_command(
        "git status --porcelain",
        "Verificando cambios en archivos"
    )
    
    # Paso 4: Mostrar estado final
    print("\n📊 RESUMEN FINAL:")
    print("=" * 30)
    
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            print(f"📝 README.md: {len(content)} caracteres")
            
            # Verificar que tiene el banner
            if "<!-- BANNER_START -->" in content and "<!-- BANNER_END -->" in content:
                print("✅ Banner encontrado en README")
            else:
                print("❌ Banner NO encontrado en README")
    
    # Verificar backups
    backup_files = [f for f in os.listdir(".") if f.startswith("README.md.backup")]
    if backup_files:
        print(f"💾 Backups encontrados: {len(backup_files)}")
        for backup in backup_files[-3:]:  # Mostrar últimos 3
            print(f"   📄 {backup}")
    
    print("\n🎉 ¡PRUEBA COMPLETADA!")
    print("🔗 Ahora puedes hacer commit y push de los cambios")
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️ Prueba interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Error crítico: {e}")
        sys.exit(1)
