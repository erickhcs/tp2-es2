class Validate:
    @staticmethod
    def empty_string(fieldName, value) -> None:
        if len(value) == 0:
            raise ValueError(f"{fieldName} parameter should not be empty!")
    
    @staticmethod
    def digit(fieldName, value) -> None:
        if not value.isdigit():
            raise ValueError(f"{fieldName} parameter should be a number!")
