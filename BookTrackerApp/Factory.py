class BookStatus:
    def status(self):
        pass

class ToRead(BookStatus):
    def status(self):
        return "To-Read"

class Reading(BookStatus):
    def status(self):
        return "Reading"

class Completed(BookStatus):
    def status(self):
        return "Completed"

class BookStatusFactory:
    @staticmethod
    def create_status(status_type):
        if status_type == "to-read":
            return ToRead()
        elif status_type == "reading":
            return Reading()
        elif status_type == "completed":
            return Completed()
        else:
            return None

# Usage
status = BookStatusFactory.create_status("reading")
print(status.status())  # Output: Reading
