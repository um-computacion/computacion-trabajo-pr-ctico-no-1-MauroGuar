[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IjdyOxY5)
# Trabajo Práctico 1: Desarrollo Guiado por Pruebas (TDD) - Conversión de Números Romanos

## Identificación del Alumno
**Nombre y Apellido:** [Completar con tu nombre y apellido]

## Objetivo
Este trabajo práctico tiene como objetivo practicar el desarrollo guiado por pruebas (TDD) en Python, implementando un convertidor de números decimales a números romanos.

## Fecha de Vencimiento
El trabajo debe ser entregado antes del **09/04/2025 a las 13:00 hs**.

## Enfoque
El trabajo se realizará en dos fases, siguiendo las prácticas de TDD:

### Fase 1: Implementación de Pruebas
En esta primera fase, deberás:
1. Crear los archivos de prueba necesarios
2. Implementar los casos de prueba para la conversión de números decimales a romanos
3. Asegurarte de que las pruebas fallen inicialmente (rojo)
4. Hacer commit y push de solo los archivos de prueba

### Fase 2: Implementación de la Solución
En la segunda fase, deberás:
1. Implementar las funciones necesarias para pasar las pruebas
2. Refactorizar el código si es necesario
3. Asegurarte de que todas las pruebas pasen (verde)
4. Hacer commit y push de la implementación

## Requisitos
- Python 3.x
- unittest (incluido en la biblioteca estándar de Python)

## Reglas de Conversión
Para la conversión de números decimales a romanos, deberás seguir estas reglas:
- Los números romanos se escriben usando las siguientes letras: I, V, X, L, C, D, M
- Los valores de las letras son:
  - I = 1
  - V = 5
  - X = 10
  - L = 50
  - C = 100
  - D = 500
  - M = 1000
- Las reglas de sustracción son:
  - I puede restar a V y X
  - X puede restar a L y C
  - C puede restar a D y M
- No se pueden usar más de tres letras iguales seguidas
- El rango de números a convertir será de 1 a 3999

## Estructura del Proyecto
```
.
├── tests/
│   └── test_roman_converter.py
└── src/
    └── roman_converter.py
```

## Entregables
1. Primer push: Archivos de prueba (`tests/test_roman_converter.py`)
2. Segundo push: Implementación completa (`src/roman_converter.py`)

## Criterios de Evaluación
- Correcta implementación de las pruebas siguiendo TDD
- Cobertura adecuada de casos de prueba
- Implementación correcta de la lógica de conversión
- Código limpio y bien estructurado
- Cumplimiento de las reglas de conversión

## Ejemplos de Uso
```python
import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()
```

## Uso del Repositorio
Para trabajar con este repositorio, es importante seguir estas pautas:

1. **No usar la opción "Add Files Via Upload"**
   - Todos los cambios deben realizarse a través de comandos git
   - Esto asegura un mejor control de versiones y seguimiento de cambios

2. **Proceso de trabajo recomendado**:
   ```bash
   # Clonar el repositorio
   git clone <url-del-repositorio>

   # Realizar cambios y commits
   git add .
   git commit -m "Descripción clara de los cambios"

   # Subir cambios al repositorio remoto
   git push origin main
   ```

3. **Commits**:
   - Primer commit: Implementación de pruebas
   - Segundo commit: Implementación de la solución
   - Cada commit debe tener un mensaje descriptivo y claro

4. **Estructura de commits**:
   - Fase 1: "Implementación de pruebas para conversión de números romanos"
   - Fase 2: "Implementación de la función decimal_to_roman"