from objectpack.observer import (  # isort:skip
    ObservableController,
    Observer,
)

observer = Observer()
controller = ObservableController(
    url='actions',
    observer=observer,
)
