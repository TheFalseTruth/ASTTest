import unittest
from TestUtils import TestAST
from AST import *
a = Id("a")
b = Id("b")
c = Id("c")
d = Id("d")
e = Id("e")
f = Id("f")
main = Id("main")
foo = Id("foo")
i1 = IntLiteral(1)
i2 = IntLiteral(2)
i3 = IntLiteral(3)
btrue = BooleanLiteral(True)
bfalse = BooleanLiteral(False)
f1 = FloatLiteral(1.1e-11)
f2 = FloatLiteral(2.2e-22)
class ASTGenSuite(unittest.TestCase):

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin end"""
        expect = str(Program([FuncDecl(main,[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_program_with_para(self):
        """Simple program: int main(paralist) {} """
        input = """procedure main(a: integer); begin end"""
        expect = str(Program([FuncDecl(main ,[VarDecl(a ,IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_program_with_more_para(self):
        """Simple program: int main(paralists) {} """
        input = """procedure main(a: integer; b: string; c: boolean); begin end"""
        expect = str(Program([FuncDecl(main ,[VarDecl(a , IntType()),VarDecl(b , StringType()),VarDecl(c , BoolType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_program_with_more_para_arraytype(self):
        """Simple program: int main(paralists) with arraytype{} """
        input = """procedure main(a: array [1 .. 2] of integer); begin end"""
        expect = str(Program([FuncDecl(main,[VarDecl(a , ArrayType(1, 2, IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_simple_program_with_more_para_arraytype_negative(self):
        """Simple program: int main(paralists) arraytype negative{} """
        input = """procedure main(a: array [-1 .. 2] of integer); begin end"""
        expect = str(Program([FuncDecl(main ,[VarDecl(a , ArrayType(-1, 2, IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_simple_program_with_more_para_arraytype_negative1(self):
        """Simple program: int main(paralists) arratype negative1{} """
        input = """procedure main(a: array [1 .. -2] of integer); begin end"""
        expect = str(Program([FuncDecl(main ,[VarDecl(a , ArrayType(1, -2, IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_simple_program_with_more_para_arraytype_negative2(self):
        """Simple program: int main(paralists) arratype negative1{} """
        input = """procedure main(a: array [-1 .. -2] of integer); begin end"""
        expect = str(Program([FuncDecl(main ,[VarDecl(a , ArrayType(-1, -2, IntType()))],[],[])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_simple_program_var_dec_only(self):
        """Simple program: var a, b """
        input = """var a, b: integer;"""
        expect = str(Program([VarDecl(a , IntType()),
                              VarDecl(b , IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_simple_program_var_dec_only_2line(self):
        """Simple program: var a, b """
        input = """var a, b: integer;
                        c, d: string;"""
        expect = str(Program([VarDecl(a, IntType()),
                              VarDecl(b, IntType()),
                              VarDecl(c, StringType()),
                              VarDecl(d, StringType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_simple_program_var_dec_only_2line_arrayType(self):
        """Simple program: var a, b
                                c, d arraytype"""
        input = """var a, b: integer;
                        c, d: array [1 .. 2] of string;"""
        expect = str(Program([VarDecl(a, IntType()),
                              VarDecl(b, IntType()),
                              VarDecl(c, ArrayType(1, 2, StringType())),
                              VarDecl(d, ArrayType(1, 2, StringType()))]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_simple_program_with_function(self):
        """Simple program: function"""
        input = """function foo(): integer; begin end"""
        expect = str(Program([FuncDecl(foo,[],[],[], IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_simple_program_with_function_with_para(self):
        """Simple program: function with para"""
        input = """function foo(a: integer; b, c: string): integer; begin end"""
        expect = str(Program([FuncDecl(foo,[VarDecl(a , IntType()),
                                                  VarDecl(b , StringType()),
                                                  VarDecl(c , StringType())],[],[], IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_simple_program_with_function_with_para_arratType(self):
        """Simple program: function with para arrayType"""
        input = """function foo(a: array [1 .. 2] of integer; b, c: string): integer; begin end"""
        expect = str(Program([FuncDecl(foo,[VarDecl(a ,ArrayType(1, 2, IntType())),
                                                  VarDecl(b, StringType()),
                                                  VarDecl(c, StringType())],[],[], IntType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_simple_program_with_function_with_para_return_array(self):
        """Simple program: function with para and return array"""
        input = """function foo(a: integer; b, c: string): array [1 .. 5] of integer; begin end"""
        expect = str(Program([FuncDecl(foo,[VarDecl(a, IntType()),
                                                  VarDecl(b, StringType()),
                                                  VarDecl(c, StringType())],[],[], ArrayType(1, 5, IntType()))]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_simple_program_with_function_with_para_var_dec(self):
        """Simple program: function with para and vardecl"""
        input = """function foo(a: integer; b, c: string): integer;
         var a: integer;
            b, c: string;
         begin end"""
        expect = str(Program([FuncDecl(foo,[VarDecl(a, IntType()),
                                                  VarDecl(b, StringType()),
                                                  VarDecl(c, StringType())],[VarDecl(a, IntType()),
                                                                                   VarDecl(b, StringType()),
                                                                                   VarDecl(c, StringType())],[], IntType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_simple_program_with_function_assignstatement(self):
        """Simple program: function with assignstatement"""
        input = """function foo(): integer;
         begin 
            a := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(a, b)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_simple_program_with_function_assignstatement1(self):
        """Simple program: function with assignstatement1"""
        input = """function foo(): integer;
         begin 
            a := b := 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(b, IntLiteral(1)),
                                                        Assign(a, b)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_simple_program_with_function_assignstatement2(self):
        """Simple program: function with assignstatement3"""
        input = """function foo(): integer;
         begin 
            a := 1;
            b := a;
            c := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(a, i1),
                                                        Assign(b, a),
                                                        Assign(c, b)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_simple_program_with_function_assignstatement_with_datatypes(self):
        """Simple program: function with assignstatement with datatypes"""
        input = """function foo(): integer;
         begin 
            a := 1;
            b := 1.1e-11;
            c := "string";
            d := true;
            e := False;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(a, i1),
                                                        Assign(b, f1),
                                                        Assign(c, StringLiteral("string")),
                                                        Assign(d, btrue),
                                                        Assign(e, bfalse)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_simple_program_with_function_assignstatement_with_complex_exp(self):
        """Simple program: function with assignstatement with complex exp"""
        input = """function foo(): integer;
         begin 
            a := a + b * foo(a[1]);
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(a, BinaryOp("+",a,
                                                                                 BinaryOp("*", b,
                                                                                          CallExpr(foo,
                                                                                                   [ArrayCell(a, i1)]))))], IntType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_simple_program_with_function_with_compoundstatement(self):
        """Simple program: function with compoundstatement"""
        input = """function foo(): integer;
         begin 
            begin
                begin
                    a := 1;
                end
            end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(a, i1)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_simple_program_with_function_with_compoundstatements_1(self):
        """Simple program: function with compoundstatement 1"""
        input = """function foo(): integer;
         begin 
            begin
                begin
                    a := 1;
                end
            end
            b := 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Assign(a, i1),
                                                        Assign(b, i1)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_simple_program_with_function_with_ifstatements(self):
        """Simple program: function with ifstatements"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                a := a + 1;
            else
                a := a - 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                           [Assign(a, BinaryOp("+", a, i1))],
                                                           [Assign(a, BinaryOp("-", a, i1))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_simple_program_with_function_with_ifstatements_without_else(self):
        """Simple program: function with ifstatements without else"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                a := a + 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                           [Assign(a, BinaryOp("+", a, i1))],
                                                           [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_simple_program_with_function_with_ifstatements_nested(self):
        """Simple program: function with ifstatements nested"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                if a < c
                then
                    a := a + 1;
                else
                    a := 1;
            else
                a := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                     [If(BinaryOp("<", a, c),
                                                         [Assign(a, BinaryOp("+", a, i1))],
                                                         [Assign(a, i1)])],
                                                     [Assign(a, b)])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_simple_program_with_function_with_ifstatements_nested_no_else(self):
        """Simple program: function with ifstatements nested without else"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                if a < c
                then
                    a := a + 1;
            else
                a := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                     [If(BinaryOp("<", a, c),
                                                         [Assign(a, BinaryOp("+", a, i1))],
                                                         [Assign(a, b)])],
                                                     [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_simple_program_with_function_with_ifstatements_nested_no_elses(self):
        """Simple program: function with ifstatements nested without else"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                if a < c
                then
                    a := a + 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                     [If(BinaryOp("<", a, c),
                                                         [Assign(a, BinaryOp("+", a, i1))],
                                                         [])],
                                                     [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_simple_program_with_function_with_ifstatements_nested_no_elses_compoundstatement(self):
        """Simple program: function with ifstatements nested without else compundstatement"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                begin
                    if a < c
                    then
                        a := a + 1;
                    else
                        a := b;
                end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                     [If(BinaryOp("<", a, c),
                                                         [Assign(a, BinaryOp("+", a, i1))],
                                                         [Assign(a, b)])],
                                                     [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_simple_program_with_function_with_ifstatements_nested_no_elses_compoundstatement1(self):
        """Simple program: function with ifstatements nested without else compundstatement1"""
        input = """function foo(): integer;
         begin 
            if a > b
            then
                begin
                a := b;
                    if a < c
                    then
                        a := a + 1;
                    else
                        a := b;
                end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[If(BinaryOp(">", a, b),
                                                     [Assign(a, b), If(BinaryOp("<", a, c),
                                                         [Assign(a, BinaryOp("+", a, i1))],
                                                         [Assign(a, b)])],
                                                     [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_simple_program_with_function_with_forstatement(self):
        """Simple program: function with forstatement"""
        input = """function foo(): integer;
         begin 
            for a := 1 to 2 do
             a := a + 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[For(a, i1, i2, True, [Assign(a, BinaryOp("+",a, i1))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_simple_program_with_function_with_forstatement_down(self):
        """Simple program: function with forstatement"""
        input = """function foo(): integer;
         begin 
            for a := 1 downto 2 do
             a := a + 1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[For(a, i1, i2, False, [Assign(a, BinaryOp("+",a, i1))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_simple_program_with_function_with_forstatement_with_compound(self):
        """Simple program: function with forstatement"""
        input = """function foo(): integer;
         begin 
            for a := 1 to 2 do
                begin
                    a := a + 1;
                    a := a;
                end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[For(a, i1, i2, True, [Assign(a, BinaryOp("+",a, i1)), Assign(a, a)])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_simple_program_with_function_with_forstatement_with_nested(self):
        """Simple program: function with forstatement"""
        input = """function foo(): integer;
         begin 
            for a := 1 to 2 do
                for a := 1.1e-11 to 2.2e-22 do
                    a := a;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[For(a, i1, i2, True, [For(a, f1, f2, True, [Assign(a, a)])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_simple_program_with_function_with_forstatement_with_nothing(self):
        """Simple program: function with forstatement"""
        input = """function foo(): integer;
         begin 
            for a := 1 to 2 do begin end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[For(a, i1, i2, True, [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_simple_program_with_function_with_whilestatement(self):
        """Simple program: function with forstatement"""
        input = """function foo(): integer;
         begin 
            while a < b do
                a := a +  1;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[While(BinaryOp("<", a, b), [Assign(a, BinaryOp("+", a, i1))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_simple_program_with_function_with_whilestatement_with_compound(self):
        """Simple program: function with whilestatement"""
        input = """function foo(): integer;
         begin 
            while a < b do
                begin
                    a := a;
                    a := a +  1;
                end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[While(BinaryOp("<", a, b), [Assign(a, a), Assign(a, BinaryOp("+", a, i1))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_simple_program_with_function_with_whilestatement_nested(self):
        """Simple program: function with whilestatement"""
        input = """function foo(): integer;
         begin 
            while a < b do
                while a > c do
                    a := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[While(BinaryOp("<", a, b), [While(BinaryOp(">", a, c), [Assign(a, b)])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_simple_program_with_function_with_whilestatement_nested_compound(self):
        """Simple program: function with whilestatement"""
        input = """function foo(): integer;
         begin 
            while a < b do
                while a > c do
                    begin
                        a := b;
                        b := a;
                    end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[While(BinaryOp("<", a, b), [While(BinaryOp(">", a, c), [Assign(a, b), Assign(b, a)])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_simple_program_with_function_with_whilestatement_nested_compound1(self):
        """Simple program: function with whilestatement"""
        input = """function foo(): integer;
         begin 
            while a < b do
                while a > c do
                    begin
                        a := b;
                        b := a;
                    end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[While(BinaryOp("<", a, b),
                                                        [While(BinaryOp(">", a, c), [Assign(a, b), Assign(b, a)])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_simple_program_with_function_with_whilestatements(self):
        """Simple program: function with whilestatements"""
        input = """function foo(): integer;
         begin 
            while a < b do
                a := b;
            while a > c do
                b := a;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[While(BinaryOp("<", a, b), [Assign(a, b)]),
                                                  While(BinaryOp(">", a, c), [Assign(b, a)])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_simple_program_with_function_with_withstatement(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin 
            with a, b: integer; do
                a := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[With([VarDecl(a, IntType()), VarDecl(b, IntType())], [Assign(a, b)])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_simple_program_with_function_with_withstatement_2line_declare(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin 
            with a, b: integer;
                    c: string; do
                a := b;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[With([VarDecl(a, IntType()), VarDecl(b, IntType()), VarDecl(c, StringType())], [Assign(a, b)])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_simple_program_with_function_with_withstatement_compound(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin 
            with a: integer; do
                begin
                    a := b;
                    b := a;
                end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[With([VarDecl(a, IntType())], [Assign(a, b), Assign(b, a)])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_simple_program_with_function_with_withstatement_nested(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin 
            with a: integer; do
                with b: string; do
                    begin end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[With([VarDecl(a, IntType())], [With([VarDecl(b, StringType())], [])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_simple_program_with_function_with_withstatement_nested_compound(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin 
            with a: integer; do
                with b: string; do
                    begin 
                        a := b;
                        b := a;
                    end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[With([VarDecl(a, IntType())], [With([VarDecl(b, StringType())], [Assign(a, b), Assign(b, a)])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_simple_program_with_function_with_withstatement_nested_compound1(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin 
            with a: integer; do
                begin
                    a := b;
                    with b: string; do
                        b := a;
                end
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[With([VarDecl(a, IntType())], [Assign(a, b), With([VarDecl(b, StringType())], [Assign(b, a)])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_simple_program_with_function_with_break(self):
        """Simple program: function with break"""
        input = """function foo(): integer;
         begin 
            break;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Break()], IntType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_simple_program_with_function_with_breaks(self):
        """Simple program: function with break"""
        input = """function foo(): integer;
         begin 
            break;
            Break;
            BREAK;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Break(), Break(), Break()], IntType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_simple_program_with_function_with_continue(self):
        """Simple program: function with continue"""
        input = """function foo(): integer;
         begin 
            continue;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Continue()], IntType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_simple_program_with_function_with_continues(self):
        """Simple program: function with continue"""
        input = """function foo(): integer;
         begin 
            continue;
            Continue;
            CONTINUE;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Continue(), Continue(), Continue()], IntType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_simple_program_with_function_with_callstatement(self):
        """Simple program: function with callstatement"""
        input = """function foo(): integer;
         begin 
            foo();
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[CallStmt(foo, [])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_simple_program_with_function_with_callstatement2(self):
        """Simple program: function with callstatement"""
        input = """function foo(): integer;
         begin 
            foo(a);
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[CallStmt(foo, [a])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_simple_program_with_function_with_callstatement3(self):
        """Simple program: function with callstatement"""
        input = """function foo(): integer;
         begin 
            foo(foo(a));
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[CallStmt(foo, [CallExpr(foo, [a])])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_simple_program_with_function_with_callstatement4(self):
        """Simple program: function with callstatement"""
        input = """function foo(): integer;
         begin 
            foo(foo(a) + foo());
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[CallStmt(foo, [BinaryOp("+", CallExpr(foo, [a]), CallExpr(foo, []))])], IntType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_simple_program_with_function_with_returnstatement(self):
        """Simple program: function with returnstatement"""
        input = """function foo(): integer;
         begin 
            return;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Return()], IntType())]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_simple_program_with_function_with_returnstatements(self):
        """Simple program: function with returnstatement"""
        input = """function foo(): integer;
         begin 
            return;
            Return;
            RETURN;
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Return(), Return(), Return()], IntType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_simple_program_with_function_with_returnstatement_with_exp(self):
        """Simple program: function with returnstatement"""
        input = """function foo(): integer;
         begin 
            return(a);
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Return(a)], IntType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_simple_program_with_function_with_returnstatement_with_exp1(self):
        """Simple program: function with returnstatement"""
        input = """function foo(): integer;
         begin 
            return(a + 1);
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Return(BinaryOp("+", a, i1))], IntType())]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_simple_program_with_function_with_returnstatement_with_exp2(self):
        """Simple program: function with returnstatement"""
        input = """function foo(): integer;
         begin 
            return(a + foo(1));
         end"""
        expect = str(Program([FuncDecl(foo,[],[],[Return(BinaryOp("+", a, CallExpr(foo, [i1])))], IntType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_simple_program_with_functions(self):
        """Simple program: functions"""
        input = """function foo(): integer; begin end
                procedure main(); begin end"""
        expect = str(Program([FuncDecl(foo,[],[],[], IntType()), FuncDecl(main, [], [], [], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_simple_program_with_functions_and_vars(self):
        """Simple program: function with vars"""
        input = """var a: integer;
                function foo(): integer; begin end
                procedure main(); begin end"""
        expect = str(Program([VarDecl(a, IntType()), FuncDecl(foo,[],[],[], IntType()), FuncDecl(main, [], [], [], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_simple_program_with_functions_and_vars1(self):
        """Simple program: function with vars"""
        input = """var a: array [-1 .. 2] of integer;
                        b: string;
                function foo(): integer; begin end
                procedure main(); begin end"""
        expect = str(Program([VarDecl(a, ArrayType(-1, 2, IntType())), VarDecl(b, StringType()), FuncDecl(foo,[],[],[], IntType()), FuncDecl(main, [], [], [], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_simple_program_with_functions_and_vars2(self):
        """Simple program: function with vars"""
        input = """var a: integer;
                function foo(): integer;
                var a: string;
                begin end
                procedure main(); 
                var b: string;
                begin end"""
        expect = str(Program([VarDecl(a, IntType()), FuncDecl(foo,[],[VarDecl(a, StringType())],[], IntType()), FuncDecl(main, [], [VarDecl(b, StringType())], [], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_simple_program_with_functions_and_vars3(self):
        """Simple program: function with vars"""
        input = """var a: integer;
                        b: string;
                function foo(): integer;
                var a: string;
                begin end
                procedure main(); 
                var b: string;
                begin end"""
        expect = str(Program([VarDecl(a, IntType()), VarDecl(b, StringType()), FuncDecl(foo,[],[VarDecl(a, StringType())],[], IntType()), FuncDecl(main, [], [VarDecl(b, StringType())], [], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_simple_program_with_functions_test_exp(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := 1 and then 2 or else 1.1e-11;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("orelse", BinaryOp("andthen", i1, i2), f1))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_simple_program_with_functions_test_exp1(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a < b;
                    a := a > b;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("<", a, b)), Assign(a, BinaryOp(">", a, b))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_simple_program_with_functions_test_exp2(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a <= b;
                    a := a >= b;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("<=", a, b)), Assign(a, BinaryOp(">=", a, b))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_simple_program_with_functions_test_exp3(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a <> b;
                    a := a = b;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("<>", a, b)), Assign(a, BinaryOp("=", a, b))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_simple_program_with_functions_test_exp4(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a + b - c or d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("or", BinaryOp("-", BinaryOp("+", a, b), c), d))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_simple_program_with_functions_test_exp5(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a / b * c;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("*", BinaryOp("/", a, b), c))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_simple_program_with_functions_test_exp6(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a div b mod c and d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("and", BinaryOp("mod", BinaryOp("div", a, b), c), d))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_simple_program_with_functions_test_exp7(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := -a;
                    a := not a;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, UnaryOp("-", a)), Assign(a, UnaryOp("not", a))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_simple_program_with_functions_test_exp8(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := 1;
                    b := 1.1e-11;
                    c := "string";
                    d := True;
                    e := False;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, i1),
                                        Assign(b, f1),
                                        Assign(c, StringLiteral("string")),
                                        Assign(d,btrue) ,
                                        Assign(e, bfalse)], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_simple_program_with_functions_test_exp10(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a + b * c;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("+", a, BinaryOp("*", b, c)))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_simple_program_with_functions_test_exp11(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a + b * c and then d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("andthen", BinaryOp("+", a, BinaryOp("*", b, c)), d))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_simple_program_with_functions_test_exp12(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a - b / c or else d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("orelse", BinaryOp("-", a, BinaryOp("/", b, c)), d))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_simple_program_with_functions_test_exp13(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a + b > c + d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp(">", BinaryOp("+", a, b), BinaryOp("+", c, d)))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_simple_program_with_functions_test_exp14(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a - b < c or d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("<", BinaryOp("-", a, b), BinaryOp("or", c, d)))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_simple_program_with_functions_test_exp15(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a - (b < c) or d;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("or", BinaryOp("-", a, BinaryOp("<", b, c)), d))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_simple_program_with_functions_test_exp16(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a - ((b < c) or d);
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("-", a,  BinaryOp("or", BinaryOp("<", b, c), d)))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_simple_program_with_functions_test_exp17(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := not a * ( a * a ) ;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("*", UnaryOp("not", a), BinaryOp("*", a, a)))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_simple_program_with_functions_test_exp18(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := not (a * ( a * a )) ;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, UnaryOp("not", BinaryOp("*", a, BinaryOp("*", a, a))))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_simple_program_with_functions_test_exp19(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := not (a * ( a * a )) > b ;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp(">", UnaryOp("not", BinaryOp("*", a, BinaryOp("*", a, a))), b))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_simple_program_with_functions_test_exp20(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := foo(foo(a), a[1]) + a;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("+",
                                                           CallExpr(foo,
                                                                    [CallExpr(foo, [a]),
                                                                     ArrayCell(a, i1)]),
                                                           a))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383   ))

    def test_simple_program_with_functions_test_exp21(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := foo(foo(a), a[1]) + a;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, BinaryOp("+",
                                                           CallExpr(foo,
                                                                    [CallExpr(foo, [a]),
                                                                     ArrayCell(a, i1)]),
                                                           a))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384   ))

    def test_simple_program_with_functions_test_exp22(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    foo(foo(a), a + (a + b - c)[1][1]);
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [CallStmt(foo, [CallExpr(foo, [a]),
                                                       BinaryOp("+", a, ArrayCell(ArrayCell(BinaryOp("-", BinaryOp("+", a, b), c),
                                                                                  i1), i1))])], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385   ))

    def test_simple_program_with_functions_test_exp23(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    foo(a[foo(a) + (a + b - c)[1][1]]);
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [CallStmt(foo, [ArrayCell(a,
                                                                 BinaryOp("+",
                                                                          CallExpr(foo, [a]),
                                                                          ArrayCell(ArrayCell(BinaryOp("-",
                                                                                                       BinaryOp("+", a, b),
                                                                                                       c), i1), i1)))])], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,386   ))

    def test_simple_program_with_functions_test_exp24(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a[foo(b, a)];
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, ArrayCell(a, CallExpr(foo, [b, a])))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387   ))

    def test_simple_program_with_functions_test_exp25(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    a := a[a[a[a[a[a]]]]];
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, ArrayCell(a, ArrayCell(a, ArrayCell(a, ArrayCell(a, ArrayCell(a, a))))))], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388   ))

    def test_simple_program_with_functions_test_exp26(self):
        """Simple program: function test exp"""
        input = """procedure main(); 
                begin 
                    foo(foo(foo()));
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [CallStmt(foo, [CallExpr(foo, [CallExpr(foo, [])])])], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389   ))

    def test_simple_program_with_functions_combine(self):
        """Simple program: function combine"""
        input = """procedure main(); 
                begin 
                    for a := foo(1) to foo(2) do
                    begin
                        a := a + 1;
                        if a > b then break;
                    end
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [For(a,
                                            CallExpr(foo, [i1]),
                                            CallExpr(foo, [i2]),
                                            True,
                                            [Assign(a, BinaryOp("+", a, i1)),
                                             If(BinaryOp(">", a, b), [Break()], []) ])], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,390   ))

    def test_simple_program_with_functions_combine1(self):
        """Simple program: function combine"""
        input = """procedure main(); 
                begin 
                    While a > b do
                        if a + 1 > b then continue; else return a;
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [While(BinaryOp(">", a, b), [If(BinaryOp(">", BinaryOp("+", a, i1), b), [Continue()], [Return(a)])])], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391   ))

    def test_simple_program_with_functions_combine2(self):
        """Simple program: function combine"""
        input = """procedure main(); 
                begin 
                    While a > b do a:= a + a[1];
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [While(BinaryOp(">", a, b), [Assign(a, BinaryOp("+", a, ArrayCell(a, i1)))])], VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392   ))

    def test_simple_program_with_functions_combine3(self):
        """Simple program: function combine"""
        input = """procedure main(); 
                begin 
                    a := "plz stop this!";
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, StringLiteral("plz stop this!"))])]))
        self.assertTrue(TestAST.test(input,expect,393   ))

    def test_simple_program_with_functions_combine4(self):
        """Simple program: function combine"""
        input = """procedure main(); 
                begin 
                    a := "plz stop this!";
                end"""
        expect = str(Program([FuncDecl(main, [], [],
                                       [Assign(a, StringLiteral("plz stop this!"))])]))
        self.assertTrue(TestAST.test(input,expect,394   ))

    def test_simple_program_with_functions_combine5(self):
        """Simple program: function combine"""
        input = """
            procedure main();
            begin
                a := 2[2];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),
                                       [],
                                       [],
                                       [Assign(a,
                                               ArrayCell(i2,i2))]
                                      )]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_simple_program_with_functions_combine6(self):
        """Simple program: function combine"""
        input = """procedure main();
		begin
            For a := foo(TRue,FALSe,TRUE) to 1 do
                BEGIN
                END
		end"""
        expect = str(Program([FuncDecl(main,[],[],
        	[For(a,CallExpr(foo,[btrue,bfalse,btrue]),i1,True,[])])]))
        self.assertTrue(TestAST.test(input,expect,396))


    def test_simple_program_with_functions_combine7(self):
        """Simple program: function combine"""
        input = """procedure main();
		    begin
                a:= TRUE and false;
		    end"""
        expect = str(Program([FuncDecl(main, [], [],
                                   [Assign(a, BinaryOp("and", btrue, bfalse))])]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_simple_program_with_functions_combine8(self):
        """Simple program: function combine"""
        input = """procedure main();
		begin
            With a: Integer; do
                foo("aaa","aaa",1,2,3,4,5);
		end"""
        expect = str(Program([FuncDecl(main,[],[],
    		[With([VarDecl(a,IntType())],[CallStmt(foo,[StringLiteral("aaa"),StringLiteral("aaa"),i1,i2,IntLiteral(3),IntLiteral(4),IntLiteral(5)])])])]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_simple_program_with_functions_combine9(self):
        """Simple program: function combine"""
        input = """procedure main();
		begin
            With a:Real; do
                if a * b THEN
                    With a:Integer ; Do
                        if a >= c THEN
                            With c:Integer ; Do
                                If a / c THEN
                                    While a = c Do
                                        A:=1;

		end"""
        expect = str(Program([FuncDecl(main,[],[],
    		[With([VarDecl(a,FloatType())],
            [If(BinaryOp("*",a, b),
            [With([VarDecl(a,IntType())],
            [If(BinaryOp(">=",a, c),
            [With([VarDecl(c,IntType())],
            [If(BinaryOp("/",a, c),
            [While(BinaryOp("=",a, c),
            [Assign(Id("A"),i1)])])])])])])])])]))
        self.assertTrue(TestAST.test(input,expect,399))

    def test_simple_program_with_functions_combine10(self):
        """Simple program: function combine"""
        input = """procedure main();
		begin
			if a > 1 then
				if a < 2 then
					b := b + 2;
				else
					b := "omaiwa";
		end"""

        expect = str(Program([FuncDecl(main,[],[],
    		[If(BinaryOp(">",a, i1),[If(BinaryOp("<",a, i2),
    			[Assign(b, BinaryOp("+",b, i2))],
    			[Assign(b,StringLiteral("omaiwa"))])]
    		)])]))
        self.assertTrue(TestAST.test(input,expect,400))
