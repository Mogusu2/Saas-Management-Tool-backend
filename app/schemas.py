from app import ma
from app.models import User, Budget, Expense, Invoice

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class BudgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Budget
        load_instance = True

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
        load_instance = True

class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        load_instance = True
