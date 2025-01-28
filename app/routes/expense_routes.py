from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.services.expense_service import ExpenseService
from app.dtos.expense_dto import ExpenseCreateDTO, ExpenseUpdateDTO, ExpenseResponseDTO

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new expense
@router.post("/", response_model=ExpenseResponseDTO)
def create_expense(expense_data: ExpenseCreateDTO, db: Session = Depends(get_db)):
    """Create a new expense entry."""
    expense_service = ExpenseService(db)
    new_expense = expense_service.create_expense(expense_data)
    return new_expense

# Get an expense by ID
@router.get("/{expense_id}", response_model=ExpenseResponseDTO)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    """Retrieve an expense by ID."""
    expense_service = ExpenseService(db)
    expense = expense_service.get_expense_by_id(expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

# Get all expenses
@router.get("/", response_model=List[ExpenseResponseDTO])
def get_all_expenses(db: Session = Depends(get_db)):
    """Retrieve all expense records."""
    expense_service = ExpenseService(db)
    return expense_service.get_all_expenses()

# Get expenses by itinerary ID
@router.get("/itinerary/{itinerary_id}", response_model=List[ExpenseResponseDTO])
def get_expenses_by_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """Retrieve all expenses for a specific itinerary."""
    expense_service = ExpenseService(db)
    return expense_service.get_expenses_by_itinerary(itinerary_id)

# Update an expense by ID
@router.put("/{expense_id}", response_model=ExpenseResponseDTO)
def update_expense(expense_id: int, expense_data: ExpenseUpdateDTO, db: Session = Depends(get_db)):
    """Update an expense by ID."""
    expense_service = ExpenseService(db)
    updated_expense = expense_service.update_expense(expense_id, expense_data)
    if updated_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense

# Delete an expense by ID
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    """Delete an expense by ID."""
    expense_service = ExpenseService(db)
    if not expense_service.delete_expense(expense_id):
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}
