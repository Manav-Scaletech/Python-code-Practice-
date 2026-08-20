from rest_framework.pagination import CursorPagination  # <-- Add this import

class MyCursorPagination(CursorPagination):             # <-- Tip: Rename your custom class so names don't conflict
    page_size = 5
    ordering = 'name'                                # <-- Set this to a valid field in your Student model
    