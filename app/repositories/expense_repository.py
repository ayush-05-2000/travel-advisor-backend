from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.dtos.expense_dto import ExpenseCreateDTO, ExpenseUpdateDTO

class ExpenseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense_data: ExpenseCreateDTO) -> Expense:
        """Creates a new expense record."""
        new_expense = Expense(**expense_data.model_dump())
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)
        return new_expense

    def get_expense_by_id(self, expense_id: int) -> Expense:
        """Fetches an expense by ID."""
        return self.db.query(Expense).filter(Expense.id == expense_id).first()

    def get_all_expenses(self):
        """Retrieves all expense records."""
        return self.db.query(Expense).all()

    def get_expenses_by_itinerary(self, itinerary_id: int):
        """Retrieves expenses linked to a specific itinerary."""
        return self.db.query(Expense).filter(Expense.itinerary_id == itinerary_id).all()

    def update_expense(self, expense_id: int, expense_data: ExpenseUpdateDTO) -> Expense:
        """Updates an existing expense record."""
        db_expense = self.get_expense_by_id(expense_id)
        if db_expense:
            for key, value in expense_data.model_dump(exclude_unset=True).items():
                setattr(db_expense, key, value)
            self.db.commit()
            self.db.refresh(db_expense)
        return db_expense

    def delete_expense(self, expense_id: int) -> bool:
        """Deletes an expense by ID."""
        db_expense = self.get_expense_by_id(expense_id)
        if db_expense:
            self.db.delete(db_expense)
            self.db.commit()
            return True
        return False
