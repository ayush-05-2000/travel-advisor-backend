from sqlalchemy.orm import Session
from app.repositories.expense_repository import ExpenseRepository
from app.dtos.expense_dto import ExpenseCreateDTO, ExpenseUpdateDTO, ExpenseResponseDTO
from typing import List, Optional

class ExpenseService:
    def __init__(self, db: Session):
        self.expense_repo = ExpenseRepository(db)

    def create_expense(self, expense_data: ExpenseCreateDTO) -> ExpenseResponseDTO:
        """Business logic to create a new expense and return a response DTO."""
        expense = self.expense_repo.create_expense(expense_data)
        return ExpenseResponseDTO.from_orm(expense)

    def get_expense_by_id(self, expense_id: int) -> Optional[ExpenseResponseDTO]:
        """Fetch expense by ID and return response DTO."""
        expense = self.expense_repo.get_expense_by_id(expense_id)
        if expense:
            return ExpenseResponseDTO.from_orm(expense)
        return None

    def get_all_expenses(self) -> List[ExpenseResponseDTO]:
        """Retrieve all expenses and return response DTOs."""
        expenses = self.expense_repo.get_all_expenses()
        return [ExpenseResponseDTO.from_orm(expense) for expense in expenses]

    def get_expenses_by_itinerary(self, itinerary_id: int) -> List[ExpenseResponseDTO]:
        """Retrieve expenses for a specific itinerary and return response DTOs."""
        expenses = self.expense_repo.get_expenses_by_itinerary(itinerary_id)
        return [ExpenseResponseDTO.from_orm(expense) for expense in expenses]

    def update_expense(self, expense_id: int, expense_data: ExpenseUpdateDTO) -> Optional[ExpenseResponseDTO]:
        """Update an expense and return the updated response DTO."""
        updated_expense = self.expense_repo.update_expense(expense_id, expense_data)
        if updated_expense:
            return ExpenseResponseDTO.from_orm(updated_expense)
        return None

    def delete_expense(self, expense_id: int) -> bool:
        """Delete an expense and return success status."""
        return self.expense_repo.delete_expense(expense_id)
