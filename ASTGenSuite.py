import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase): 
    
    def test_var_1(self):
        input = """
            var a:integer;
            """
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,1))

    def test_var_2(self):
        input = """
            var a,b:integer;
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,2))

    def test_var_3(self):
        input = """
            var a:integer;
                b:integer;
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,3))

    def test_var_4(self):
        input = """
            var a,b:integer;
                b:integer;
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,4))

    def test_var_5(self):
        input = """
            var a:integer;
            var b:integer;
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,5))

    def test_var_6(self):
        input = """
            var a,b:integer;
            var b:integer;
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,6))

    def test_var_7(self):
        input = """
            var a: array [1 .. 2] of integer;
            """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,7))

    def test_var_8(self):
        input = """
            var a,b: array [1 .. 2] of integer;
            """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,IntType())),VarDecl(Id("b"),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,8))

    def test_var_9(self):
        input = """
            var a: array [1 .. 2] of integer;
                b: array [1 .. 2] of integer;
            """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,IntType())),VarDecl(Id("b"),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,9))

    def test_var_10(self):
        input = """
            var a: array [1 .. 2] of integer;
            var b: array [1 .. 2] of integer;
            """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,IntType())),VarDecl(Id("b"),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,10))


    def test_procedure_1(self):
        input = """
            procedure main();
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,11))

    def test_procedure_2(self):
        input = """
            procedure main();
            var a:integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,12))

    def test_procedure_3(self):
        input = """
            procedure main();
            var a,b:integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,13))

    def test_procedure_4(self):
        input = """
            procedure main();
            var a:integer;
                b:integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,14))

    def test_procedure_5(self):
        input = """
            procedure main();
            var a:array [1 .. 2] of integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),ArrayType(1,2,IntType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,15))
    def test_procedure_6(self):
        input = """
            procedure main();
            var a,b:array [1 .. 2] of integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),ArrayType(1,2,IntType())),VarDecl(Id("b"),ArrayType(1,2,IntType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,16))
    def test_procedure_7(self):
        input = """
            procedure main();
            var a:array [1 .. 2] of integer;
                b:array [1 .. 2] of string;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),ArrayType(1,2,IntType())),VarDecl(Id("b"),ArrayType(1,2,StringType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,17))

    def test_procedure_8(self):
        input = """
            procedure main(a:integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,18))

    def test_procedure_9(self):
        input = """
            procedure main(a,b:integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,19))

    def test_procedure_10(self):
        input = """
            procedure main(a:integer;b:integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,20))

    def test_procedure_11(self):
        input = """
            procedure main(a,b:integer;c:integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,21))

    def test_procedure_12(self):
        input = """
            procedure main(a:array [1 .. -2] of integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayType(1,-2,IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,22))

    def test_procedure_13(self):
        input = """
            procedure main(a,b:array [-1 .. 2] of integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayType(-1,2,IntType())),VarDecl(Id("b"),ArrayType(-1,2,IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,23))

    def test_procedure_14(self):
        input = """
            procedure main(a:array [1 .. 2] of integer;b:array [1 .. 2] of integer);
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayType(1,2,IntType())),VarDecl(Id("b"),ArrayType(1,2,IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,24))

    def test_statement_1(self):
        input = """
            procedure main();
            begin 
                break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Break()])]))
        self.assertTrue(TestAST.test(input,expect,25))

    def test_statement_2(self):
        input = """
            procedure main();
            begin 
                continue;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Continue()])]))
        self.assertTrue(TestAST.test(input,expect,26))

    def test_statement_3(self):
        input = """
            procedure main();
            begin 
                break;
                continue;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Break(),Continue()])]))
        self.assertTrue(TestAST.test(input,expect,27))

    def test_statement_4(self):
        input = """
            procedure main();
            begin 
                break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Break()])]))
        self.assertTrue(TestAST.test(input,expect,28))

    def test_statement_5(self):
        input = """
            procedure main();
            begin 
                a := 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,29))

    def test_statement_6(self):
        input = """
            procedure main();
            begin 
                a := b;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),Id("b"))])]))
        self.assertTrue(TestAST.test(input,expect,30))

    def test_statement_7(self):
        input = """
            procedure main();
            begin 
                a := b := 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("b"),IntLiteral(1)),Assign(Id("a"),Id("b"))])]))
        self.assertTrue(TestAST.test(input,expect,31))

    def test_statement_8(self):
        input = """
            procedure main();
            begin 
                a[1] := 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,32))

    def test_statement_9(self):
        input = """
            procedure main();
            begin 
                a[1] := b[a] := 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(Id("b"),Id("a")),IntLiteral(1)), Assign(ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),Id("a")))])]))
        self.assertTrue(TestAST.test(input,expect,33))

    def test_statement_10(self):
        input = """
            procedure main();
            begin 
                a[1] := b[a];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),Id("a")))])]))
        self.assertTrue(TestAST.test(input,expect,34))

    def test_statement_11(self):
        input = """
            procedure main();
            begin 
                a()[1] := 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1)),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,35))

    def test_statement_12(self):
        input = """
            procedure main();
            begin 
                a := 1 + 2;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),
                                       [],
                                       [],
                                       [Assign(Id("a"),
                                               BinaryOp("+",IntLiteral(1),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,36))

    def test_statement_13(self):
        input = """
            procedure main();
            begin 
                a := 1 + 2*3;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),IntLiteral(3))))])]))
        self.assertTrue(TestAST.test(input,expect,37))

    def test_statement_14(self):
        input = """
            procedure main();
            begin 
                a := b[c];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),ArrayCell(Id("b"),Id("c")))])]))
        self.assertTrue(TestAST.test(input,expect,38))

    def test_statement_15(self):
        input = """
            procedure main();
            begin 
                a := b()[c];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),ArrayCell(CallExpr(Id("b"),[]),Id("c")))])]))
        self.assertTrue(TestAST.test(input,expect,39))

    def test_statement_16(self):
        input = """
            procedure main();
            begin 
                a := (2)[c];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),ArrayCell(IntLiteral(2),Id("c")))])]))
        self.assertTrue(TestAST.test(input,expect,40))

    def test_statement_17(self):
        input = """
            procedure main();
            begin 
                a := b(2)[c];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),ArrayCell(CallExpr(Id("b"),[IntLiteral(2)]),Id("c")))])]))
        self.assertTrue(TestAST.test(input,expect,41))

    def test_statement_18(self):
        input = """
            procedure main();
            begin 
                a := (1+2)*3 - 10;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(10)))])]))
        self.assertTrue(TestAST.test(input,expect,42))

    def test_statement_19(self):
        input = """
            procedure main();
            begin 
                a := (2)[c] + 2;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),BinaryOp("+",ArrayCell(IntLiteral(2),Id("c")),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,43))

    def test_statement_20(self):
        input = """
            procedure main();
            begin 
                while a < 1 do return;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("<",Id("a"),IntLiteral(1)),[Return(None)])])]))
        self.assertTrue(TestAST.test(input,expect,44))

    def test_statement_21(self):
        input = """
            procedure main();
            begin 
                while a < 1 do begin break; continue; end
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("<",Id("a"),IntLiteral(1)),[Break(),Continue()])])]))
        self.assertTrue(TestAST.test(input,expect,45))

    def test_statement_22(self):
        input = """
            procedure main();
            begin 
                if a < 1 then break; else continue;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(1)),[Break()],[Continue()])])]))
        self.assertTrue(TestAST.test(input,expect,46))

    def test_statement_23(self):
        input = """
            procedure main();
            begin 
                if a < 1 then begin break; continue; end
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(1)),[Break(),Continue()],[])])]))
        self.assertTrue(TestAST.test(input,expect,47))

    def test_statement_24(self):
        input = """
            procedure main();
            begin 
                for a:= 1 to 2 do continue;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(1),IntLiteral(2),True,[Continue()])])]))
        self.assertTrue(TestAST.test(input,expect,48))

    def test_statement_25(self):
        input = """
            procedure main();
            begin 
                for a:= 1 to 2 do begin continue; break; end
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(1),IntLiteral(2),True,[Continue(),Break()])])]))
        self.assertTrue(TestAST.test(input,expect,49))

    def test_statement_26(self):
        input = """
            procedure main();
            begin 
                with a:integer; do break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),IntType())],[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,50))

    def test_statement_27(self):
        input = """
            procedure main();
            begin 
                with a,b:integer; do break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,51))

    def test_statement_28(self):
        input = """
            procedure main();
            begin 
                with a:integer;b:integer; do break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,52))

    def test_statement_29(self):
        input = """
            procedure main();
            begin 
                with a,b:integer;c:integer; do break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,53))

    def test_statement_30(self):
        input = """
            procedure main();
            begin 
                with a:integer; do begin break; continue; end
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),IntType())],[Break(),Continue()])])]))
        self.assertTrue(TestAST.test(input,expect,54))

    def test_statement_31(self):
        input = """
            procedure main();
            begin 
                with a:array [-1 .. -2] of integer; do break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),ArrayType(-1,-2,IntType()))],[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,55))

    def test_statement_32(self):
        input = """
            procedure main();
            begin 
                foo();
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[])])]))
        self.assertTrue(TestAST.test(input,expect,56))

    def test_statement_33(self):
        input = """
            procedure main();
            begin 
                foo(a);
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[Id("a")])])]))
        self.assertTrue(TestAST.test(input,expect,57))

    def test_statement_34(self):
        input = """
            procedure main();
            begin 
                foo(2);
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[IntLiteral(2)])])]))
        self.assertTrue(TestAST.test(input,expect,58))

    def test_statement_35(self):
        input = """
            procedure main();
            begin 
                foo(1,2);
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2)])])]))
        self.assertTrue(TestAST.test(input,expect,59))

    def test_statement_36(self):
        input = """
            procedure main();
            begin 
                foo(1,2+3);
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[IntLiteral(1),BinaryOp("+",IntLiteral(2),IntLiteral(3))])])]))
        self.assertTrue(TestAST.test(input,expect,60))

    def test_statement_37(self):
        input = """
            procedure main();
            begin 
                return;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Return(None)])]))
        self.assertTrue(TestAST.test(input,expect,61))

    def test_statement_38(self):
        input = """
            procedure main();
            begin 
                RETURN 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[Return(IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,62))

    def test_statement_39(self):
        input = """
            procedure main();
            begin 
                if 1 and then 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("andthen",IntLiteral(1),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,63))

    def test_statement_40(self):
        input = """
            procedure main();
            begin 
                if 1 or else 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("orelse",IntLiteral(1),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,64))

    def test_statement_41(self):
        input = """
            procedure main();
            begin 
                if 1 = 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("=",IntLiteral(1),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,65))

    def test_statement_42(self):
        input = """
            procedure main();
            begin 
                if True = 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("=",BooleanLiteral(True),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,66))

    def test_statement_43(self):
        input = """
            procedure main();
            begin 
                if False = 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("=",BooleanLiteral(False),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,67))

    def test_statement_44(self):
        input = """
            procedure main();
            begin 
                if TRUE = FaLse then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("=",BooleanLiteral(True),BooleanLiteral(False)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,68))

    def test_statement_45(self):
        input = """
            procedure main();
            begin 
                if "string" = 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("=",StringLiteral("string"),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,69))

    def test_statement_46(self):
        input = """
            procedure main();
            begin 
                if 1.2 = 2 then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("=",FloatLiteral("1.2"),IntLiteral(2)),[Break()])])]))
        self.assertTrue(TestAST.test(input,expect,70))

    def test_statement_47(self):
        input = """
            procedure main();
            begin 
                if a < 1 then if b > 2 then break; else continue;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(1)),
                                                            [If(BinaryOp(">",Id("b"),IntLiteral(2)),[Break()],[Continue()])],[])])]))
        self.assertTrue(TestAST.test(input,expect,71))

    def test_statement_48(self):
        input = """
            procedure main();
            begin 
                if a < 1 then begin if b > 2 then break; continue; end else continue;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(1)),
                                                            [If(BinaryOp(">",Id("b"),IntLiteral(2)),[Break()]), Continue()],[Continue()])])]))
        self.assertTrue(TestAST.test(input,expect,72))

    def test_statement_49(self):
        input = """
            procedure main();
            begin 
                if a AND b then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("AND",Id("a"),Id("b")),[Break()],[])])]))
        self.assertTrue(TestAST.test(input,expect,73))

    def test_statement_50(self):
        input = """
            procedure main();
            begin 
                if a[1] AND b then break;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("AND",ArrayCell(Id("a"),IntLiteral(1)),Id("b")),[Break()],[])])]))
        self.assertTrue(TestAST.test(input,expect,74))

    def test_statement_51(self):
        input = """
            procedure main();
            begin 
                foo(a[1]);
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[ArrayCell(Id("a"),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,75))

    def test_statement_52(self):
        input = """
            procedure main();
            begin 
                foo(a,a,a,a);
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[Id("a"),Id("a"),Id("a"),Id("a")])])]))
        self.assertTrue(TestAST.test(input,expect,76))

    def test_statement_53(self):
        input = """
            procedure main();
            begin 
                if a < 1 then a := b := 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("<",Id("a"),IntLiteral(1)),[Assign(Id("b"),IntLiteral(1)),Assign(Id("a"),Id("b"))])])]))
        self.assertTrue(TestAST.test(input,expect,77))

    def test_var_11(self):
        input = """
            function main():integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,78))

    def test_var_12(self):
        input = """
            function main():string;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,79))

    def test_var_13(self):
        input = """
            function main():array [1 .. 2] of integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,80))

    def test_var_14(self):
        input = """
            procedure main();
            var a:integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,81))

    def test_var_15(self):
        input = """
            procedure main();
            var a,b:integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,82))

    def test_var_16(self):
        input = """
            procedure main();
            var a:integer; b:integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,83))

    def test_var_17(self):
        input = """
            procedure main();
            var a,b:integer; c:integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,84))

    def test_var_18(self):
        input = """
            procedure main();
            var a:array [1 .. 2] of boolean;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),ArrayType(1,2,BoolType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,85))


    def test_var_19(self):
        input = """
            function main():boolean;
            begin             end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,86))

    def test_var_20(self):
        input = """
            function main():string;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,87))

    def test_statement_64(self):
        input = """
            function main():integer;
            var a:integer;
            begin 
                RETURN 1;
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Return(IntLiteral(1))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,88))

    def test_statement_65(self):
        input = """
            var a:integer;
            procedure main();
            begin 
            end
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,89))

    def test_statement_66(self):
        input = """
            procedure main();
            begin 
            end
            var a:integer;
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[]),VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,90))

    def test_statement_67(self):
        input = """
            var a,b:integer;
            procedure main();
            begin 
            end
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,91))

    def test_statement_68(self):
        input = """
            var a:integer; b:integer;
            procedure main();
            begin 
            end
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,92))

    def test_statement_69(self):
        input = """
            var a:integer;
            var b:integer;
            procedure main();
            begin 
            end
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,93))

    def test_statement_70(self):
        input = """
            procedure main();
            begin 
            end
            function main():integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[]),FuncDecl(Id("main"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,94))

    def test_statement_71(self):
        input = """
            var a:integer;
            function main():integer;
            begin 
            end
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),FuncDecl(Id("main"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,95))

    def test_statement_72(self):
        input = """
            var a,b:integer;
            function main():integer;
            begin 
            end
            """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),FuncDecl(Id("main"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,96))

    def test_statement_73(self):
        input = """
            function main(a:integer):integer;
            begin end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,97))

    def test_statement_74(self):
        input = """
            function main(a,b:integer):integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,98))

    def test_statement_75(self):
        input = """
            function main(a:integer;b:integer):integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,99))

    def test_statement_76(self):
        input = """
            function main(a:array [1 .. 2] of integer):integer;
            begin 
            end
            """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayType(1,2,IntType()))],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,100))

    def test_statement_77(self):
        input = """
            procedure main();
            begin begin begin end begin end end end
            """
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,101))