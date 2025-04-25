# PG2.Practica3

# API Diagnósticos Especiales en la Infancia  

## 📌 Introducción  
Esta API proporciona información sobre el diagnóstico y la intervención de condiciones mentales en la infancia. Su objetivo es facilitar la identificación de síntomas y ofrecer apoyo emocional y profesional para padres y maestros.  

## 🛠️ Autenticación  
- **Método:** Mediante una clave de API  
- **Encabezado requerido:** `Authorization: Bearer <API_KEY>`  

## 📊 Endpoints  

### 🔍 Diagnóstico Infantil  
**Descripción:** Proporciona información detallada sobre diversas condiciones mentales que afectan a la población infantil.  
**Parámetros:**  
- `condicion`: Tipo de diagnóstico a consultar  
**Datos proporcionados:**  
- Descripción general de la condición  
- Síntomas característicos  
- Edad promedio de diagnóstico  

### 📝 Identificación de Síntomas  
**Descripción:** Ofrece puntos clave para reconocer síntomas en niños según su edad y comportamiento.  
**Parámetro opcional:**  
- `edad`: Filtra síntomas comunes según la edad del niño  
**Datos proporcionados:**  
- Lista de síntomas frecuentes  
- Factores de riesgo asociados  

### 🤝 Apoyo para Padres y Maestros  
**Descripción:** Brinda estrategias de intervención y apoyo emocional para quienes acompañan a niños con condiciones mentales.  
**Parámetro requerido:**  
- `rol`: Puede ser `"padre"` o `"maestro"`  
**Datos proporcion