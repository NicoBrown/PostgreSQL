import psycopg2
import pytermgui as ptg

# Connect to chinook database using connect method
connection = psycopg2.connect(database="chinook")

# set cursor up to accept commands
cursor = connection.cursor()

# cursor commands
cursor.execute('SELECT * FROM "Artist"')

# method used to fetch all results
results = cursor.fetchall()

# placehodler method to collect one result
# results = cursor.fetchone()

# close connection
connection.close()


def run_Terminal_GUI():
    CONFIG = """
    config:
        InputField:
            styles:
                prompt: dim italic
                cursor: '@72'
        Label:
            styles:
                value: dim bold

        Window:
            styles:
                border: '60'
                corner: '60'

        Container:
            styles:
                border: '96'
                corner: '96'
    """

    with ptg.YamlLoader() as loader:
        loader.load(CONFIG)

    with ptg.WindowManager() as manager:
        window = (
            ptg.Window(
                "",
                "Search the Music Database here by entering\na value into one of the inputs and press enter:",
                "",
                ptg.InputField(" ", prompt="Album: "),
                ptg.InputField(" ", prompt="Artist: "),
                ptg.InputField(" ", prompt="Genre: "),
                ptg.InputField(" ", prompt="Track: "),
                "",
                ptg.Button("submit"),
                ["Submit", lambda *_: submit(manager, window)],
                width=60,
                box="DOUBLE",
            )
            .set_title("[210 bold]Music Database Search")
            .center()
        )

        manager.add(window)

run_Terminal_GUI()

for result in results:
    print(result)

