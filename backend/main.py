from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
from ml import predict_category

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Finance AI")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add-expense", response_model=schemas.ExpenseResponse)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):

    category = predict_category(expense.description)

    db_expense = models.Expense(
        description=expense.description,
        amount=expense.amount,
        category=category
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    return db_expense


@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()

    data = {}
    for e in expenses:
        data[e.category] = data.get(e.category, 0) + e.amount

    return data
