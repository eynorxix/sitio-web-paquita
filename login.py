import flet as ft

def main(page: ft.Page):
    page.title = "Gestor de Inventario - Tienda"
    page.theme_mode = "light"
    page.padding = 20
    page.window_width = 1200
    page.window_height = 800

    # Datos de ejemplo (productos)
    productos = [
        {"id": 1, "nombre": "Laptop", "stock": 15, "precio": 1200},
        {"id": 2, "nombre": "Mouse", "stock": 50, "precio": 20},
        {"id": 3, "nombre": "Teclado", "stock": 30, "precio": 50},
        {"id": 4, "nombre": "Monitor", "stock": 25, "precio": 300},
        {"id": 5, "nombre": "USB 64GB", "stock": 100, "precio": 15},
        {"id": 6, "nombre": "Auriculares", "stock": 40, "precio": 80},
        {"id": 7, "nombre": "Impresora", "stock": 10, "precio": 200},
        {"id": 8, "nombre": "Disco SSD", "stock": 35, "precio": 90},
        {"id": 9, "nombre": "Webcam", "stock": 20, "precio": 60},
        {"id": 10, "nombre": "Router", "stock": 18, "precio": 70},
        {"id": 11, "nombre": "Altavoz", "stock": 22, "precio": 45},
        {"id": 12, "nombre": "Tablet", "stock": 12, "precio": 250},
    ]

    # Barra de búsqueda
    buscador = ft.TextField(
        hint_text="Buscar producto...",
        width=400,
        prefix_icon=ft.icons.SEARCH,
        border_radius=20,
    )

    # Cuadrícula de productos (5 columnas × 4 filas)
    grid_productos = ft.GridView(
        expand=True,
        runs_count=5,  # Columnas
        max_extent=200,  # Ancho de cada tarjeta
        spacing=10,
        run_spacing=10,
    )

    # Panel lateral (información de stock)
    panel_stock = ft.Column(
        expand=True,
        spacing=10,
        controls=[
            ft.Text("Niveles de Stock", size=18, weight="bold"),
            ft.Divider(),
        ],
    )

    # Función para actualizar la cuadrícula de productos
    def actualizar_productos():
        grid_productos.controls.clear()
        for producto in productos:
            grid_productos.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(producto["nombre"], weight="bold"),
                                ft.Text(f"Stock: {producto['stock']}"),
                                ft.Text(f"Precio: ${producto['precio']}"),
                            ],
                            spacing=5,
                        ),
                        padding=10,
                    ),
                    elevation=5,
                )
            )
        page.update()

    # Función para actualizar el panel de stock
    def actualizar_stock():
        panel_stock.controls = [
            ft.Text("Niveles de Stock", size=18, weight="bold"),
            ft.Divider(),
        ]
        for producto in productos:
            panel_stock.controls.append(
                ft.Text(f"{producto['nombre']}: {producto['stock']} unidades")
            )
        page.update()

    # Llamamos a las funciones para cargar los datos
    actualizar_productos()
    actualizar_stock()

    # Diseño principal (buscador + grid + panel lateral)
    page.add(
        ft.Row([buscador], alignment="center"),
        ft.Row(
            [
                ft.Column([grid_productos], expand=3),
                ft.VerticalDivider(),
                ft.Column([panel_stock], expand=1),
            ],
            expand=True,
        ),
    )

ft.app(target=main)