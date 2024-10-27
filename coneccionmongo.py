from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://eramirez13:SuSerNFNzHMSKB1a@desarrolloweb.nclk9.mongodb.net/?retryWrites=true&w=majority&appName=Desarrolloweb"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Seleccionar la base de datos y la colección
db = client["Desarrolloweb"]
coleccion = db["Departamentos"]

departamentos = [
    {
        "nombre": "Amazonas",
        "capital": "Leticia",
        "poblacion": 82068,
        "area_km2": 109665,
        "municipios": [
            "Leticia", "Puerto Nariño", "La Chorrera", "Tarapacá", "Puerto Santander", "El Encanto", "Mirití-Paraná",
            "Puerto Alegría", "Puerto Arica", "La Pedrera"]
    },
    {
        "nombre": "Arauca",
        "capital": "Arauca",
        "poblacion": 304978,
        "area_km2": 23818,
        "municipios": [
            "Arauca", "Arauquita", "Cravo Norte", "Fortul", "Puerto Rondón", "Saravena", "Tame"]
    },
    {
        "nombre": "Antioquia",
        "capital": "Medellín",
        "poblacion": 6887306,
        "area_km2": 63612,
        "municipios": [
            "Medellín", "Bello", "Envigado", "Itagüí", "Rionegro", "Apartadó", "Turbo", "La Ceja", "Caucasia", 
            "Sabaneta", "Marinilla", "Santa Fe de Antioquia", "Puerto Berrío", "Yarumal", "Necoclí"],
    },
    {
        "nombre": "Atlántico",
        "capital": "Barranquilla",
        "poblacion": 2804025,
        "area_km2": 3388,
        "municipios": [
            "Barranquilla", "Soledad", "Malambo", "Galapa", "Baranoa", "Sabanalarga", "Santo Tomás", "Polonuevo", 
            "Ponedera", "Juan de Acosta", "Campo de la Cruz", "Palmar de Varela"]
    },
    {
        "nombre": "Bogotá",
        "capital": "Bogotá",
        "poblacion": 8906342,
        "area_km2": 1775,
        "municipios": ["Bogotá"]
    },
    {
        "nombre": "Bolívar",
        "capital": "Cartagena",
        "poblacion": 2236603,
        "area_km2": 25978,
        "municipios": [
            "Cartagena", "Magangué", "El Carmen de Bolívar", "Mompós", "Turbaco", "Arjona", "Santa Rosa de Lima", 
            "San Estanislao", "Mahates", "María la Baja", "Santa Catalina", "San Juan Nepomuceno", "Cicuco", "Calamar"]
    },
    {
        "nombre": "Boyacá",
        "capital": "Tunja",
        "poblacion": 1259601,
        "area_km2": 23189,
        "municipios": [
            "Tunja", "Duitama", "Sogamoso", "Chiquinquirá", "Samacá", "Paipa", "Villa de Leyva", "Moniquirá", "Soatá", 
            "Santa Rosa de Viterbo", "Ráquira", "Nobsa", "Tota", "Chita"]
    },
    {
        "nombre": "Caldas",
        "capital": "Manizales",
        "poblacion": 1036455,
        "area_km2": 7888,
        "municipios": [
            "Manizales", "Villamaría", "La Dorada", "Chinchiná", "Riosucio", "Anserma", "Pensilvania", "Neira", 
            "Salamina", "Aguadas", "Supía", "Marulanda", "Manzanares", "Samaná"]
    },
    {
        "nombre": "Caquetá",
        "capital": "Florencia",
        "poblacion": 419275,
        "area_km2": 88965,
        "municipios": [
            "Florencia", "La Montañita", "Morelia", "El Paujil", "San Vicente del Caguán", "Solano", "Puerto Rico", 
            "Solita", "Albania", "Valparaíso", "Curillo"]
    },
    {
        "nombre": "Casanare",
        "capital": "Yopal",
        "poblacion": 442068,
        "area_km2": 44640,
        "municipios": [
            "Yopal", "Aguazul", "Maní", "Paz de Ariporo", "Villanueva", "Tauramena", "Monterrey", "Trinidad", 
            "Orocué", "San Luis de Palenque", "Nunchía", "Recetor", "Hato Corozal", "Sácama", "La Salina", "Chámeza"]
    },
    {
        "nombre": "Cauca",
        "capital": "Popayán",
        "poblacion": 1516018,
        "area_km2": 29108,
        "municipios": [
            "Popayán", "Santander de Quilichao", "Puerto Tejada", "Guapi", "El Tambo", "Timbiquí", "Inzá", "Caloto", 
            "Patía", "Mercaderes", "Piendamó", "Balboa", "Toribío", "Silvia"]
    },
    {
        "nombre": "Cesar",
        "capital": "Valledupar",
        "poblacion": 1341697,
        "area_km2": 22905,
        "municipios": [
            "Valledupar", "Aguachica", "Bosconia", "Curumaní", "Codazzi", "La Jagua de Ibirico", "Chimichagua", 
            "El Paso", "San Alberto", "Becerril", "Astrea", "La Gloria"]
    },
    {
        "nombre": "Chocó",
        "capital": "Quibdó",
        "poblacion": 553519,
        "area_km2": 46630,
        "municipios": [
            "Quibdó", "Istmina", "Condoto", "Tadó", "Bahía Solano", "Acandí", "Riosucio", "Cértegui", "El Carmen de Atrato", 
            "Nuquí", "Bojayá", "Medio Atrato", "Lloró"]
    },
    {
        "nombre": "Córdoba",
        "capital": "Montería",
        "poblacion": 1856496,
        "area_km2": 25020,
        "municipios": [
            "Montería", "Lorica", "Cereté", "Sahagún", "Tierralta", "Ciénaga de Oro", "Planeta Rica", "San Pelayo", 
            "Pueblo Nuevo", "San Carlos", "Los Córdobas", "Ayapel"]
    },
    {
        "nombre": "Cundinamarca",
        "capital": "Bogotá",
        "poblacion": 2473634,
        "area_km2": 22982,
        "municipios": [
            "Soacha", "Fusagasugá", "Girardot", "Zipaquirá", "Chía", "Cajicá", "Facatativá", "Mosquera", "Madrid", 
            "Funza", "La Mesa", "Tocancipá", "Villeta", "Tenjo", "Anapoima"]
    },
    {
        "nombre": "Guainía",
        "capital": "Inírida",
        "poblacion": 52061,
        "area_km2": 72238,
        "municipios": [
            "Inírida", "Barrancominas", "Mapiripana", "San Felipe", "La Guadalupe", "Cacahual", "Pana Pana"]
    },
    {
        "nombre": "Guaviare",
        "capital": "San José del Guaviare",
        "poblacion": 90357,
        "area_km2": 53384,
        "municipios": [
            "San José del Guaviare", "El Retorno", "Calamar", "Miraflores"]
    },
    {
        "nombre": "Huila",
        "capital": "Neiva",
        "poblacion": 1140932,
        "area_km2": 19389,
        "municipios": [
            "Neiva", "Pitalito", "Garzón", "La Plata", "Campoalegre", "San Agustín", "Isnos", "Palermo", "Algeciras", 
            "Rivera", "Aipe", "Tello", "Yaguará"]
    },
    {
        "nombre": "La Guajira",
        "capital": "Riohacha",
        "poblacion": 1002394,
        "area_km2": 20848,
        "municipios": [
            "Riohacha", "Maicao", "Uribia", "Fonseca", "San Juan del Cesar", "Dibulla", "Hatonuevo", "Barrancas", 
            "Villanueva", "El Molino", "Distracción", "Manaure"]
    },
    {
        "nombre": "Magdalena",
        "capital": "Santa Marta",
        "poblacion": 1463427,
        "area_km2": 23823,
        "municipios": [
            "Santa Marta", "Ciénaga", "Fundación", "El Banco", "Aracataca", "Pivijay", "Plato", "Santa Ana", 
            "Zona Bananera", "Salamina", "San Sebastián de Buenavista", "Remolino", "Tenerife", "Sitio Nuevo"]
    },
    {
        "nombre": "Meta",
        "capital": "Villavicencio",
        "poblacion": 1080706,
        "area_km2": 85335,
        "municipios": [
            "Villavicencio", "Acacías", "Granada", "Puerto López", "Cumaral", "San Martín", "Puerto Gaitán", 
            "Castilla La Nueva", "El Dorado", "Guamal", "San Carlos de Guaroa", "Fuente de Oro", "Puerto Concordia"]
    },
    {
        "nombre": "Nariño",
        "capital": "Pasto",
        "poblacion": 1629181,
        "area_km2": 33820,
        "municipios": [
            "Pasto", "Tumaco", "Ipiales", "Tuquerres", "Samaniego", "La Cruz", "El Charco", "La Tola", 
            "Santa Bárbara", "Leiva", "Policarpa", "Sandoná", "Pupiales", "San Lorenzo"]
    },
    {
        "nombre": "Norte de Santander",
        "capital": "Cúcuta",
        "poblacion": 1651278,
        "area_km2": 21658,
        "municipios": [
            "Cúcuta", "Ocaña", "Pamplona", "Los Patios", "Villa del Rosario", "Tibú", "El Zulia", 
            "Ábrego", "Chinácota", "Convención", "San Calixto", "Sardinata", "La Playa", "Puerto Santander"]
    },
    {
        "nombre": "Putumayo",
        "capital": "Mocoa",
        "poblacion": 369064,
        "area_km2": 24885,
        "municipios": [
            "Mocoa", "Puerto Asís", "Orito", "Puerto Leguízamo", "Sibundoy", "Colón", "San Francisco", 
            "Villagarzón", "Puerto Guzmán", "San Miguel", "Valle del Guamuez"]
    },
    {
        "nombre": "Quindío",
        "capital": "Armenia",
        "poblacion": 569569,
        "area_km2": 1845,
        "municipios": [
            "Armenia", "Calarcá", "Quimbaya", "Montenegro", "La Tebaida", "Salento", "Circasia", 
            "Filandia", "Génova", "Buenavista", "Pijao"]
    },
    {
        "nombre": "Risaralda",
        "capital": "Pereira",
        "poblacion": 977829,
        "area_km2": 4140,
        "municipios": [
            "Pereira", "Dosquebradas", "Santa Rosa de Cabal", "La Virginia", "Belén de Umbría", 
            "Apía", "Marsella", "Quinchía", "Mistrató", "Santuario", "Guática", "Balboa"]
    },
    {
        "nombre": "San Andrés y Providencia",
        "capital": "San Andrés",
        "poblacion": 65228,
        "area_km2": 52,
        "municipios": ["San Andrés", "Providencia"]
    },
    {
        "nombre": "Santander",
        "capital": "Bucaramanga",
        "poblacion": 2324090,
        "area_km2": 30536,
        "municipios": [
            "Bucaramanga", "Barrancabermeja", "Floridablanca", "Girón", "Piedecuesta", "San Gil", 
            "Socorro", "Lebrija", "Rionegro", "Vélez", "Barbosa", "Cimitarra", "Sabana de Torres", 
            "Zapatoca"]
    },
    {
        "nombre": "Sucre",
        "capital": "Sincelejo",
        "poblacion": 972350,
        "area_km2": 10917,
        "municipios": [
            "Sincelejo", "Corozal", "Sampués", "San Marcos", "San Onofre", "Tolú", "Coveñas", 
            "Chalán", "Palmito", "Majagual", "Morroa", "Ovejas"]
    },
    {
        "nombre": "Tolima",
        "capital": "Ibagué",
        "poblacion": 1346935,
        "area_km2": 23562,
        "municipios": [
            "Ibagué", "Espinal", "Melgar", "Honda", "Líbano", "Mariquita", "Flandes", 
            "Chaparral", "Rovira", "Guamo", "Planadas", "Purificación"]
    },
    {
        "nombre": "Valle del Cauca",
        "capital": "Cali",
        "poblacion": 4589278,
        "area_km2": 22140,
        "municipios": [
            "Cali", "Buenaventura", "Palmira", "Tuluá", "Cartago", "Jamundí", "Buga", "Yumbo", 
            "Florida", "Candelaria", "Dagua", "Ginebra", "Guacarí"]
    },
    {
        "nombre": "Vaupés",
        "capital": "Mitú",
        "poblacion": 48932,
        "area_km2": 54410,
        "municipios": ["Mitú", "Carurú", "Pacoa", "Taraira", "Yavaraté"]
    },
    {
        "nombre": "Vichada",
        "capital": "Puerto Carreño",
        "poblacion": 115778,
        "area_km2": 100242,
        "municipios": ["Puerto Carreño", "La Primavera", "Santa Rosalía", "Cumaribo"]
    }
]


# Insertar los documentos en la colección
resultado = coleccion.insert_many(departamentos)

# Imprimir los IDs de los documentos insertados
print("Documentos insertados con IDs:", resultado.inserted_ids)