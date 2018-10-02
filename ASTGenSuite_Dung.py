import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var a,b,c:integer;
                        d:real;
                    var e,r,t:string;"""
        expect = """Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),StringType),VarDecl(Id(r),StringType),VarDecl(Id(t),StringType)])"""
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple2_function(self):
        """More complex program"""
        input = """function foo (xxx:INTEGER):INTEGER; begin
            if a < b then
                a[1][1+2]:=1;
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("xxx"),
                    IntType())],[],[If(BinaryOp("<",Id("a"),Id("b")),
                    [Assign(ArrayCell(ArrayCell(Id("a"),IntLiteral(1)),
                    BinaryOp("+",IntLiteral(1),IntLiteral(2))),IntLiteral(1))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple3_function(self):
        """More complex program"""
        input = """procedure foo(xxx:INTEGER);begin
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("xxx"),IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_defFunctWithForLoop(self):
        """More complex program"""
        input = """function foo():INTEGER;
        begin
            for iii := 1 to 1000 do
                begin
                end
        end
        """
        expect = str(Program([
                FuncDecl(Id("foo"),[],[],[For(Id("iii"),IntLiteral(1),IntLiteral(1000),True,[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_defFunctWithForWhile(self):
        """More complex program"""
        input = """function foo():INTEGER;
        begin
            while a < b do
                begin
                end
        end
        """
        expect = str(Program([
                FuncDecl(Id("foo"),[],[],[While(BinaryOp('<',Id("a"),Id("b")),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))


    def test_defFunctWithForWith(self):
        """More complex program"""
        input = """function foo():INTEGER;
        begin
            with a:INTEGER; do
                begin
                end
        end
        """
        expect = str(Program([
                FuncDecl(Id("foo"),[],[],[With([VarDecl(Id("a"),IntType())],[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_defFunctWithCallStmt(self):
        """More complex program"""
        input = """
        function foo():INTEGER;
        begin
            bebe(1);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[],[CallStmt( Id("bebe"), [IntLiteral(1)] ) ], IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_defFunctWithAssignStmt(self):
        """More complex program"""
        input = """
        function foo():INTEGER;
        begin
            a:=b:=c:=1;
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[],
                [Assign(Id("c"),IntLiteral(1)),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))], IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_defFunctWithAssignStmtAndFuncall(self):
        """More complex program"""
        input = """
        function foo():INTEGER;
        begin
            a:=b:=c:=foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[],
                [Assign(Id("c"),CallExpr(Id("foo"),[IntLiteral(2)])),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))], IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_defFunctWithAssignStmtAndExp(self):
        """More complex program"""
        input = """
        function foo():INTEGER;
        begin
            a:=(2+3)* 10 - 1;
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[],
                [Assign(Id("a"),BinaryOp('-',BinaryOp('*',BinaryOp('+',IntLiteral(2),IntLiteral(3)),IntLiteral(10)),IntLiteral(1)))
                ],
                IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_defProce(self):
        """More complex program"""
        input = """
        procedure foo();
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_defProce_para(self):
        """More complex program"""
        input = """
        procedure foo(a:INTEGER);
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[VarDecl(Id("a"),IntType())],[],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_defProce_manypara(self):
        """More complex program"""
        input = """
        procedure foo(a:REAL;b:INTEGER);
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],[],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_defProce_localPara(self):
        """More complex program"""
        input = """
        procedure foo();
        var a:INTEGER;
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[VarDecl(Id("a"),IntType())],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_defProce_localmanyPara(self):
        """More complex program"""
        input = """
        procedure foo();
        var a:REAL; b:INTEGER;
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_deffunc_localmanyPara(self):
        """More complex program"""
        input = """
        procedure foo();
        var a:REAL;
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[VarDecl(Id("a"),FloatType())],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_deffunc_localmanyPara(self):
        """More complex program"""
        input = """
        procedure foo();
        var a:REAL;b:INTEGER;
        begin
            foo(2);
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                )]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_defmanyfunc(self):
        """More complex program"""
        input = """
        function foo():INTEGER;
        begin
            foo(2);
        end
        function foo1():INTEGER;
        begin
        end
        """
        expect = str(Program([
                FuncDecl( Id("foo"),[],[],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                ,IntType()),FuncDecl( Id("foo1"),[],[],
                [],IntType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_defmanyDelVar(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        vAr b:STRING;
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_defVarFunVar1(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            foo(2);
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [CallStmt(Id("foo"),[IntLiteral(2)])]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_defProceIfandelse(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            if a<b then
            a:=1;
            else
            a:=2;
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [If(BinaryOp("<",Id("a"),Id("b")),
                [Assign(Id("a"),IntLiteral(1))],
                [Assign(Id("a"),IntLiteral(2))]
                )
                ])
                ,VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_defFuncIfandFor1(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            if a<b then
                for i:= 100 to 1000 do
                begin
                end
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [If(BinaryOp("<",Id("a"),Id("b")),
                [For(Id("i"),IntLiteral(100),IntLiteral(1000),True,[])]
                )])
                ,VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_defFuncIfandWhile(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            if a<b then
            WhIle a<b do
            a:=1;
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [If(BinaryOp("<",Id("a"),Id("b")),
                [While(BinaryOp("<",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(1))])]
                )])
                ,VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_defFuncIfandWith1(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            if a<b then
                with a:INTEGER ;do
                    begin
                    end
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [If(BinaryOp("<",Id("a"),Id("b")),
                [With([VarDecl(Id("a"),IntType())],[])]
                ,[])])
                ,VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_defFuncIndexVocal(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            a:=a[a+b][a/2];
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [Assign(Id("a"),ArrayCell(ArrayCell(Id("a"),BinaryOp("+",Id("a"),Id("b"))),BinaryOp("/",Id("a"),IntLiteral(2))))]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_defProceFor_AndIf(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            for i:=1000 DownTo 0 do
                if a <> b then
                begin
                end
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [For(Id("i"),IntLiteral(1000),IntLiteral(0),False,[If(BinaryOp("<>",Id("a"),Id("b")),[])])]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_defProceForandWhile(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            for i:=1000 DownTo 0 do
                while a >= b do
                begin
                end
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [For(Id("i"),IntLiteral(1000),IntLiteral(0),False,[While(BinaryOp(">=",Id("a"),Id("b")),[])])]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_defFuncForAndFor(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            for i:=1000 DownTo 0 do
                for i:=1000 DownTo 0 do
                begin
                end
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [For(Id("i"),IntLiteral(1000),IntLiteral(0),False,[For(Id("i"),IntLiteral(1000),IntLiteral(0),False,[])])]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,328))


#Check agian , ... some problem here
    def test_defFuncWhileandWhile(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            while a AND b do
                while a Or b do
                    begin
                    end
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [While(BinaryOp("AND",Id("a"),Id("b")),[While(BinaryOp("Or",Id("a"),Id("b")),[])])]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_defFuncWithAnd____With(self):
        """More complex program"""
        input = """
        var a:INTEGER;
        procedure foo();
        begin
            with a:String ; do
                with a:BOOLEAN; do
                    a:=1;
        end
        var b:REAL;
        """
        expect = str(Program([
                VarDecl(Id("a"),IntType()),
                FuncDecl( Id("foo"),[],[],
                [With([VarDecl(Id("a"),StringType())],[With([VarDecl(Id("a"),BoolType())],[Assign(Id("a"),IntLiteral(1))])])]
                ),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_defFuncWithAnd__With(self):
        """More complex program"""
        input = """function foo(a: integer):real;
    	var c: integer;
    	d: real;
    	begin
    	a := b := 9;
    	end
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],
        [VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType())],
        [Assign(Id("b"),IntLiteral(9)),Assign(Id("a"),Id("b"))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_defFuncForAnd__ForAssignString(self):
        """More complex program"""
        input = """function foo(a: integer):real;
    	var c: string;
    	d: real;
    	begin
        	for i:= 0 to 1000 do
                c := c +"abcd";
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),StringType()),VarDecl(Id("d"),FloatType())],
        [For(Id("i"),IntLiteral(0),IntLiteral(1000),True,[Assign(Id("c"),BinaryOp("+",Id("c"),StringLiteral("abcd")))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_defFuncForAnd__Expr(self):
        """More complex program"""
        input = """function foo(a: integer):real;
    	var c: string;
    	d: real;
    	begin
        	For i:=0-1 To 1000+1000 do
                begin end
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),StringType()),VarDecl(Id("d"),FloatType())],
        [For(Id("i"),BinaryOp("-",IntLiteral(0),IntLiteral(1)),BinaryOp("+",IntLiteral(1000),IntLiteral(1000)),True,[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_defFuncAssign_StringInWhileLoop(self):
        """More complex program"""
        input = """function foo(a: integer):real;
    	var c: string;
    	d: real;
    	begin
            while a <= b do
                cd:="AAAAA";
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),StringType()),VarDecl(Id("d"),FloatType())],
        [While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("cd"),StringLiteral("AAAAA"))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_defProceWhile_LoopW(self):
        """More complex program"""
        input = """Procedure foo(a: integer);
    	var c: string;
    	d: real;
    	begin
        	while a-b do
                begin end

    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),StringType()),VarDecl(Id("d"),FloatType())],
        [While(BinaryOp("-",Id("a"),Id("b")),[])])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_defProceIfAndIfAndIfAnd__Assign(self):
        """More complex program"""
        input = """Procedure foo(a: integer);
    	var c: integer;
    	d: real;
    	begin
        	if a>b then
                if a<b then
                    if c<b THEN
                        a:=1;


    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType())],
        [If(BinaryOp(">",Id("a"),Id("b")),[If(BinaryOp("<",Id("a"),Id("b")),[If(BinaryOp("<",Id("c"),Id("b")),[Assign(Id("a"),IntLiteral(1)) ]  )] )] ) ] ) ] ) )
        self.assertTrue(TestAST.test(input,expect,336))

    def test_defProce__AssignWithVoCalAndExp(self):
        """More complex program"""
        input = """procedure foo(a: integer);
    	var c: INTEGER;
    	d: real;
    	begin
            a:=a[a+b][a]+123;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType())],
        [Assign(Id("a"),BinaryOp("+",ArrayCell(ArrayCell(Id("a"),BinaryOp("+",Id("a"),Id("b"))),Id("a")),IntLiteral(123)))])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_defProce__Proce(self):
        """More complex program"""
        input = """
        procedure foo(a: integer);
    	   var c: INTEGER;
    	      d: real;
    	        begin
    	         end
        procedure foo1(a:integer);
            begin end
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType())],
                []),FuncDecl(Id("foo1"),[VarDecl(Id("a"),IntType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,338))


    def test_defProcMany_For(self):
        """More complex program"""
        input = """procedure foo();

    	begin
        	For i:=0 To 1000 do
            begin end
            For i:=1000 To 2000 do
            begin end
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [For(Id("i"),IntLiteral(0),IntLiteral(1000),True,[]),For(Id("i"),IntLiteral(1000),IntLiteral(2000),True,[])])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_defProcManyWhile_Loop(self):
        """More complex program"""
        input = """procedure foo();

    	begin
        	While a<>b do
                a:=a+b;
            While a<=10 do
                a:=1 mod 2;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [While(BinaryOp("<>",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]),While(BinaryOp("<=",Id("a"),IntLiteral(10)),
        [Assign(Id("a"),BinaryOp("mod",IntLiteral(1),IntLiteral(2)))])])]))

        self.assertTrue(TestAST.test(input,expect,340))

    def test_defProc_Many_If(self):
        """More complex program"""
        input = """procedure foo();
    	begin
            if a<b then
            a:=a mod 10;
            if a>b then
            a:=b - a;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [If(BinaryOp("<",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("mod",Id("a"),IntLiteral(10)))],[] ),If(BinaryOp(">",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",Id("b"),Id("a")))],[])])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_defFunctReturn_ArrayType(self):
        input = """ function foo(): Array[ 1 .. 1 ] of Integer;
    	begin
            hello:="Ahihi Do^ Ngo^\\' k";
            a:=b - a;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [Assign(Id("hello"),StringLiteral("Ahihi Do^ Ngo^\\' k")),
        Assign(Id("a"),BinaryOp("-",Id("b"),Id("a")))],
        ArrayType(1,1,IntType()) ) ]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_defProceVarArrayDeclPara(self):
        input = """procedure foo(a:array[-1 .. 1] of INteger);
    	begin
            a:=b-a;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),
        [VarDecl(Id("a"),ArrayType(-1,1,IntType()))],[],
        [Assign(Id("a"),BinaryOp("-",Id("b"),Id("a")))])]))

        self.assertTrue(TestAST.test(input,expect,343))

    def test_defProcDeclArrayLocal1(self):
        input = """procedure foo();
        var a: Array[ 1 .. -1] of Integer;
    	begin
    	end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("a"),ArrayType(1,-1,IntType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_declArray1(self):
        input = """var a:array[1 .. 1] of Integer;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,1,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_defmanyArray(self):
        input = """
        var a:Array[1 .. -1] of Integer;
        var b: array[-1 .. -1] of String;
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,-1,IntType())),VarDecl(Id("b"),ArrayType(-1,-1,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_defDeclFunctWithReturn(self):
        input = """function foo():Real;
    	begin
            return ;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [Return()],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_defProcReturnInFor(self):
        input = """procedure foo();
    	begin
            for i:=1 Downto 10+10 do
                return ;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [For(Id("i"),IntLiteral(1),BinaryOp("+",IntLiteral(10),IntLiteral(10)),False,[Return()])])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_defProcforWithReturnExp(self):
        input = """procedure foo();
    	begin
            For i:=0 To 1000 do
                return a+b;
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [For(Id("i"),IntLiteral(0),IntLiteral(1000),True,[Return(BinaryOp("+",Id("a"),Id("b")))])])]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_defProcWhileWithRetunrExpAndFunCallExp(self):
        input = """procedure foo();
    	begin
            While a Or b do
                return a+foo(2);
    	end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],
        [While(BinaryOp("Or",Id("a"),Id("b")),[Return(BinaryOp("+",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])) )])])
        ]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_if_within_if_1(self):
    	input = """procedure proc();
		begin

			if a > 3 then
            begin
				if a < 7 then
					b := b + 2;
				else
					foo(1);
            end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[If(BinaryOp(">",Id("a"),IntLiteral(3)),[If(BinaryOp("<",Id("a"),IntLiteral(7)),
    			[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))],[CallStmt(Id("foo"),[IntLiteral(1)])])])])]))
    	self.assertTrue(TestAST.test(input,expect,351))

    def test_ProceContinueInFor(self):
    	input = """procedure proc();
		begin
            For i:=0 to 1000 do
                BEGIN
                    a:=1;
                    continue;
                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(0),IntLiteral(1000),True,[Assign(Id("a"),IntLiteral(1)),Continue()])])]))
    	self.assertTrue(TestAST.test(input,expect,352))

    def test_ProceContinueInWhile(self):
    	input = """procedure proc();
		begin
            While a+2 do
                begin
                    foo(2);
                    continue;
                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[While(BinaryOp("+",Id("a"),IntLiteral(2)),[CallStmt(Id("foo"),[IntLiteral(2)]),Continue()])])]))
    	self.assertTrue(TestAST.test(input,expect,353))

    def test_ProceContinueInForAndFor(self):
    	input = """procedure proc();
		begin
            for i:=1 to 100 do
                for i:=0 to 1000 do
                    BEGIN
                        k:=1;
                        continue;
                    end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(1),IntLiteral(100),True,[For(Id("i"),IntLiteral(0),IntLiteral(1000),True,[Assign(Id("k"),IntLiteral(1)),Continue()])])])]))
    	self.assertTrue(TestAST.test(input,expect,354))

    def test_ProceContinueWhileAndWhile(self):
    	input = """procedure proc();
		begin
            While a mod b do
                while a mod 3 do
                    continue;
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[While(BinaryOp("mod",Id("a"),Id("b")),[While(BinaryOp("mod",Id("a"),IntLiteral(3)),[Continue()])])])]))
    	self.assertTrue(TestAST.test(input,expect,355))

    def test_BreakInFor(self):
    	input = """procedure proc();
		begin
            for i:=1 to 1000 do
                BEGIN
                    a:=1+2;
                    break;
                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(1),IntLiteral(1000),True,[Assign(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2))),Break()])])]))
    	self.assertTrue(TestAST.test(input,expect,356))

    def test_BreakInForAndFor(self):
    	input = """procedure proc();
		begin
            For i:= 0 to 100 do
                for i:=1 to 1000 do
                Begin
                    a:=100;
                    Break;
                End

		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(0),IntLiteral(100),True,[For(Id("i"),IntLiteral(1),IntLiteral(1000),True,[Assign(Id("a"),IntLiteral(100)),Break()])])])]))
    	self.assertTrue(TestAST.test(input,expect,357))


    def test_BreakAndContinueIn_While(self):
    	input = """procedure proc();
		begin
            While (a+b-c)+a do
            begin
                break;
                continue;
            end


		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[While(BinaryOp("+",BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("a")),[Break(),Continue()])])]))
    	self.assertTrue(TestAST.test(input,expect,358))

    def test_BreakAndContinueInFor(self):
    	input = """procedure proc();
		begin
            For i:=1000 downTo 2 do
                BEGIN
                    Break;
                    CoNTiNue;
                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(1000),IntLiteral(2),False,[Break(),Continue()])])]))
    	self.assertTrue(TestAST.test(input,expect,359))

    def test_ExpInDex(self):
    	input = """procedure proc();
		begin
            foo(a[a][a+b]);

		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[CallStmt(Id("foo"),[ArrayCell(ArrayCell(Id("a"),Id("a")),BinaryOp("+",Id("a"),Id("b")))])])]))
    	self.assertTrue(TestAST.test(input,expect,360))

    def test_ForAndCallInExp(self):
    	input = """procedure proc();
		begin
            for i:=foo(2) to foo(2) + foo(3) do
                BEGIN

                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),CallExpr(Id("foo"),[IntLiteral(2)]),
            BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(2)]),CallExpr(Id("foo"),[IntLiteral(3)])),True,[])])]))
    	self.assertTrue(TestAST.test(input,expect,361))


    def test_ForAndForAndIfAndBreak(self):
    	input = """procedure proc();
		begin
            for i:=0 to 100 do
                for i:=0 to 100 do
                    if a<b then
                    begin
                        a:=1;
                        break;
                    end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(0),IntLiteral(100),True,
            [For(Id("i"),IntLiteral(0),IntLiteral(100),True,
            [If(BinaryOp("<",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(1)),Break()]
            )])])])]))
    	self.assertTrue(TestAST.test(input,expect,362))

    def test_ForAnd_IfElse(self):
    	input = """procedure proc();
		begin
            for i:=0 to 100 do
                if a<b then
                    a:=1;
                ELSE
                    Break;
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),IntLiteral(0),IntLiteral(100),True,[If(BinaryOp("<",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(1))],[Break()])])])]))
    	self.assertTrue(TestAST.test(input,expect,363))

    def test_CallStmtWithDownArgument(self):
    	input = """procedure proc();
		begin
            foo();
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[CallStmt(Id("foo"),[])])]))
    	self.assertTrue(TestAST.test(input,expect,364))

    def test_CallExpWithoutArgumentInfor(self):
    	input = """procedure proc();
		begin
            for i:=foo() to foo() do
                begin
                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[]),True,[])])]))
    	self.assertTrue(TestAST.test(input,expect,365))

    def test_CallExpWithoutArgumentInfor(self):
    	input = """procedure proc();
		begin
            for i:=foo() to foo() do
                begin
                end
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[For(Id("i"),CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[]),True,[])])]))
    	self.assertTrue(TestAST.test(input,expect,366))

    def test_IfElseInIfElse(self):
    	input = """procedure proc();
		begin
            If a<b then
                if c>d then
                    a:=1;
                else
                    a:=2;
            else
            a:=3;

		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[If(BinaryOp("<",Id("a"),Id("b")),[If(BinaryOp(">",Id("c"),Id("d")),[Assign(Id("a"),IntLiteral(1))],
            [Assign(Id("a"),IntLiteral(2))])],[Assign(Id("a"),IntLiteral(3))])])]))
    	self.assertTrue(TestAST.test(input,expect,366))


    def test_ComplexExpression(self):
    	input = """procedure proc();
		begin
            a:=a And c Or d And Then e;

		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[Assign(Id("a"),BinaryOp("andthen",BinaryOp("Or",BinaryOp("And",Id("a"),Id("c")),Id("d")),Id("e")))])]))
    	self.assertTrue(TestAST.test(input,expect,367))

    def test_ComplexExpression_1(self):
    	input = """procedure proc();
		begin
            a:= ( a div b ) div c;

		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[Assign(Id("a"),BinaryOp("div",BinaryOp("div",Id("a"),Id("b")),Id("c")))])]))
    	self.assertTrue(TestAST.test(input,expect,368))

    def test_ComplexExpression_3(self):
    	input = """procedure proc();
		begin
            a:=-(NOT(-b));
		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[Assign(Id("a"),UnaryOp('-',UnaryOp('NOT',UnaryOp('-',Id("b")))))])]))
    	self.assertTrue(TestAST.test(input,expect,369))

    def test_ComplexExpression_4(self):
    	input = """procedure proc();
		begin
            a:= c - (-d);

		end"""
    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[Assign(Id("a"),BinaryOp('-',Id("c"),UnaryOp("-",Id("d"))))])]))
    	self.assertTrue(TestAST.test(input,expect,370))

    def test_for_in_while(self):
    	input = """procedure main();
		begin
		while foo() do
			for i := 0 to 1+1 do
				a := a + 1;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[While(CallExpr(Id("foo"),[]),
    			[For(Id("i"),IntLiteral(0),BinaryOp("+",IntLiteral(1),IntLiteral(1)),True,
    				[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])])])]))
    	self.assertTrue(TestAST.test(input,expect,371))

    def test_ifAndFor__(self):
    	input = """procedure main();
		begin
		while foo() do
			for i := 0 to 1+1 do
				a := a + 1;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[While(CallExpr(Id("foo"),[]),
    			[For(Id("i"),IntLiteral(0),BinaryOp("+",IntLiteral(1),IntLiteral(1)),True,
    				[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])])])]))
    	self.assertTrue(TestAST.test(input,expect,372))

    def test_Func_If_Else_While_For_With(self):
    	input = """procedure main();
		begin
		while foo() do
			for i := 0 to 1+1 do
				a := a + 1;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[While(CallExpr(Id("foo"),[]),
    			[For(Id("i"),IntLiteral(0),BinaryOp("+",IntLiteral(1),IntLiteral(1)),True,
    				[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])])])]))
    	self.assertTrue(TestAST.test(input,expect,373))

    def test_Func_FOr_ManyBeginEndAndNoTHingInside(self):
    	input = """procedure main();
		begin
			for i := 0 to 1+1 do
				BEGIN
                    BEGIN
                        BEGIN
                        ENd
                    END
                ENd
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    			[For(Id("i"),IntLiteral(0),BinaryOp("+",IntLiteral(1),IntLiteral(1)),True,
    			        [])])]))
    	self.assertTrue(TestAST.test(input,expect,374))

    def test_Func_ManyBeginEndInBody(self):
    	input = """function main():real;
		begin
	       Begin
           END
           BEGIN
           END
           BEGIN
           END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[],FloatType())]))
    	self.assertTrue(TestAST.test(input,expect,375))

    def test_ProceDuree_ManyBeginEnd_LOOP_InBody(self):
    	input = """procedure main();
		begin
            BEGIN
                BEGIN
                    BEGIN
                    END
                END
            END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[])]))
    	self.assertTrue(TestAST.test(input,expect,376))

    def test_Funct_ManyBeginEnd_LOOP_InBody(self):
    	input = """function main():STRING;
		begin
	         BEGIN
                BEGIN
                    BEGIN
                    end
                END
             END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[],StringType())]))
    	self.assertTrue(TestAST.test(input,expect,377))

    def test_Procedure_ManyBeginEnd_InBody(self):
    	input = """procedure main();
		begin
            BEGIN
                BEGIN
                    BEGIN
                    End
                END
            END

		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[])]))
    	self.assertTrue(TestAST.test(input,expect,378))

    def test_Procedure_ManyBeginEnd_InForLoopWithAssignEach(self):
    	input = """procedure main();
		begin
            For i:=1 to 100 do
            BEGIN
                a:=100;
                BEGIN
                    b:=100;
                    BEGIN
                        c:=200;
                    END
                END
            END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[For(Id("i"),IntLiteral(1),IntLiteral(100),True,[Assign(Id("a"),IntLiteral(100)),Assign(Id("b"),IntLiteral(100)),Assign(Id("c"),IntLiteral(200))])])]))
    	self.assertTrue(TestAST.test(input,expect,379))

    def test_Procedure_ManyBeginEnd_InBodyOfFor(self):
    	input = """procedure main();
		begin
			for i := 0 to 1+1 do
    			BEGIN
                    BEGIN
                    END
                    BEGIN
                    END
                    BEGIN
                    END
                    BEGIN
                        a:=100;
                    END
                END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    			[For(Id("i"),IntLiteral(0),BinaryOp("+",IntLiteral(1),IntLiteral(1)),True,
    				[Assign(Id("a"),IntLiteral(100))])])]))
    	self.assertTrue(TestAST.test(input,expect,380))

    def test_Procedure_ManyBeginEnd_InBodyWithAssign(self):
    	input = """procedure main();
		begin
            BEGIN
                a:=100;
            END
            BEGIN
                b:=200;
            ENd
            BEGIN
                c:=300;
            End
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[Assign(Id("a"),IntLiteral(100)),Assign(Id("b"),IntLiteral(200)),Assign(Id("c"),IntLiteral(300))])]))
    	self.assertTrue(TestAST.test(input,expect,381))

    def test_Procedure_WhileAndManyBeginEnd(self):
    	input = """procedure main();
		begin
		while foo() do
			BEGIN
                ass:=100;

            END
        BEGIN
            foo(2);
        END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[While(CallExpr(Id("foo"),[]),[Assign(Id("ass"),IntLiteral(100))]),CallStmt(Id("foo"),[IntLiteral(2)])])]))
    	self.assertTrue(TestAST.test(input,expect,382))

    def test_Procedure_ForAndManyBeginEnd(self):
    	input = """procedure main();
		begin
            for i:=0 to 1+1 do
                BEGIN
                    BEGIN
                        a:=1+1;
                    ENd
                    a:=1000;
                END

		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    			[For(Id("i"),IntLiteral(0),BinaryOp("+",IntLiteral(1),IntLiteral(1)),True,
    				[Assign(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1))),Assign(Id("a"),IntLiteral(1000))])])]))
    	self.assertTrue(TestAST.test(input,expect,383))

    def test_Procedure_WithAndManyBeginEnd(self):
    	input = """procedure main();
		begin
            With a:Real ; do
                BEGIN
                    BEGIN
                        a:=100;
                    END
                    BEGIN
                        foo(a[2][2]);
                    End
                END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),FloatType())],[Assign(Id("a"),IntLiteral(100)),CallStmt(Id("foo"),[ArrayCell(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(2))])])])]))
    	self.assertTrue(TestAST.test(input,expect,384))

    def test_Procedure_IfAndManyBeginEnd(self):
    	input = """procedure main();
		begin
	         If(a > b) then
             BEGIN
                BEGIN
                    a:=100;
                END
             End
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[If(BinaryOp(">",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(100))])])]))
    	self.assertTrue(TestAST.test(input,expect,385))

    def test_if_within_if_1_2(self):
    	input = """procedure proc();
		begin
			if a > 3 then
				if a < 7 then
					b := b + 2;
				else
					b := "huhuhuhuhu";
		end"""

    	expect = str(Program([FuncDecl(Id("proc"),[],[],
    		[If(BinaryOp(">",Id("a"),IntLiteral(3)),[If(BinaryOp("<",Id("a"),IntLiteral(7)),
    			[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))],
    			[Assign(Id("b"),StringLiteral("huhuhuhuhu"))])]
    		)])]))
    	self.assertTrue(TestAST.test(input,expect,386))

    def test_Procedure_WithDeclareArray(self):
    	input = """procedure main();
		begin
            with a,b,c: array[-1 .. 1] of String; do
            Begin
                A:=1;
            End

		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),ArrayType(-1,1,StringType())),VarDecl(Id("b"),ArrayType(-1,1,StringType())),VarDecl(Id("c"),ArrayType(-1,1,StringType()))]
            ,[Assign(Id("A"),IntLiteral(1))])])]))
    	self.assertTrue(TestAST.test(input,expect,386))

    def test_Procedure_WithManyDeclare(self):
    	input = """procedure main();
		begin
            WiTh a:Integer; c:Array[1 .. 1] of Integer; do
            BEGIN
                Foo(1);
            END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),IntType()),VarDecl(Id("c"),ArrayType(1,1,IntType()))],[CallStmt(Id("Foo"),[IntLiteral(1)])])])]))
    	self.assertTrue(TestAST.test(input,expect,387))

    def test_Procedure_WithAndWithAndIf(self):
    	input = """procedure main();
		 BEGIN
            With a:Real ; Do
                With b:Integer; Do
                    If a<b Then
                        a:=1;
                    Else
                        A:=2;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),FloatType())],
            [With([VarDecl(Id("b"),IntType())],
            [If(BinaryOp("<",Id("a"),Id("b")),[Assign(Id("a"),IntLiteral(1))],[Assign(Id("A"),IntLiteral(2))])
            ])])])]))
    	self.assertTrue(TestAST.test(input,expect,388))

    def test_Procedure_WithAndIfAndWith(self):
    	input = """procedure main();
		begin
            With a:Integer; do
                if a<b then
                    With a:Real;
                    do
                        a:=a[2+2][2+9];
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),IntType())],[If(BinaryOp("<",Id("a"),Id("b")),[With([VarDecl(Id("a"),FloatType())],
            [Assign(Id("a"),ArrayCell(ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),IntLiteral(2))),BinaryOp("+",IntLiteral(2),IntLiteral(9))))])])])])]))
    	self.assertTrue(TestAST.test(input,expect,389))

    def test_Procedure_WithAndIfAndWithAndIfAndWhile(self):
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
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),FloatType())],
            [If(BinaryOp("*",Id("a"),Id("b")),
            [With([VarDecl(Id("a"),IntType())],
            [If(BinaryOp(">=",Id("a"),Id("c")),
            [With([VarDecl(Id("c"),IntType())],
            [If(BinaryOp("/",Id("a"),Id("c")),
            [While(BinaryOp("=",Id("a"),Id("c")),
            [Assign(Id("A"),IntLiteral(1))])])])])])])])])]))
    	self.assertTrue(TestAST.test(input,expect,390))

    def test_CallStmtWithStringInput(self):
    	input = """procedure main();
		begin
            With a:Integer; do
                foo("aaa");
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[StringLiteral("aaa")])])])]))
    	self.assertTrue(TestAST.test(input,expect,391))

    def test_CallStmtWithManyInput(self):
    	input = """procedure main();
		begin
            With a:Integer; do
                foo("aaa","aaa",1,2,3,4,5);
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[With([VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[StringLiteral("aaa"),StringLiteral("aaa"),IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])])])]))
    	self.assertTrue(TestAST.test(input,expect,392))

    def test_TestOperandFloatType(self):
    	input = """procedure main();
		begin
            a:=1.2+ 1.3 + 4.1;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[Assign(Id("a"),BinaryOp("+",BinaryOp("+",FloatLiteral(1.2),FloatLiteral(1.3)),FloatLiteral(4.1)))])]))
    	self.assertTrue(TestAST.test(input,expect,393))

    def test_TestCallExprInputFloatType(self):
    	input = """procedure main();
		begin
            for i:= foo(1.e100) to 100 do
                a:=1;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[For(Id("i"),CallExpr(Id("foo"),[FloatLiteral(1.e100)]),IntLiteral(100),True,[Assign(Id("a"),IntLiteral(1))])])]))
    	self.assertTrue(TestAST.test(input,expect,394))

    def test_TestCallstmtrInputFloatType(self):
    	input = """procedure main();
		begin
            foo(1.e199999);
            return;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[CallStmt(Id("foo"),[FloatLiteral(1.e199999)]),Return()])]))
    	self.assertTrue(TestAST.test(input,expect,395))

    def test_TestOperandBOOLEAN(self):
    	input = """procedure main();
		begin
            a:= TRUE and false;
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[Assign(Id("a"),BinaryOp("and",BooleanLiteral(True),BooleanLiteral(False)))])]))
    	self.assertTrue(TestAST.test(input,expect,396))

    def test_TestCallWithInputBoolean(self):
    	input = """procedure main();
		begin
            foo(TRuE, False, TrUe);
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[CallStmt(Id("foo"),[BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])])]))
    	self.assertTrue(TestAST.test(input,expect,397))

    def test_TestCallStmtWithInputBoolean(self):
    	input = """procedure main();
		begin
            For i:=Foo(TRue,FALSe,TRUE) to 1000 do
                BEGIN
                END
		end"""
    	expect = str(Program([FuncDecl(Id("main"),[],[],
    		[For(Id("i"),CallExpr(Id("Foo"),[BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]),IntLiteral(1000),True,[])])]))
    	self.assertTrue(TestAST.test(input,expect,398))

    def test_Done_In_AFewDaysWithFewsHoursOfSleep____Exhausted__2_MORE_LEFT__WAITING__(self):
    	input = """procedure Exhausted();
		begin
            a:= "TheEnd 00:54 29 September 2018 :) :) :) :)";
		end"""
    	expect = str(Program([FuncDecl(Id("Exhausted"),[],[],
    		[Assign(Id("a"),StringLiteral("TheEnd 00:54 29 September 2018 :) :) :) :)"))])]))
    	self.assertTrue(TestAST.test(input,expect,399))

    def test_call_func_with_index_expression(self):
    	input = """function foo(a: integer):integer;
    	var h: array [-10 .. 10] of integer;
    	begin

    	end"""
    	expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],
    		[VarDecl(Id("h"),ArrayType(-10,10,IntType()))],
    		[],IntType())]))
    	self.assertTrue(TestAST.test(input,expect,400))

    def test_call_exp_in_while__(self):
    	input = """function foo(a: real):string;
    	var h: string;
    	begin
    		while true do
        		ugh := boring(a = "empty")[not a + b];
    	end"""
    	expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType())],
    		[VarDecl(Id("h"),StringType())],
    		[While(BooleanLiteral(True),[Assign(Id("ugh"),ArrayCell(CallExpr(Id("boring"),
    			[BinaryOp("=",Id("a"),StringLiteral("empty"))]),BinaryOp("+",UnaryOp("not",Id("a")),Id("b"))))])],StringType())]))
    	self.assertTrue(TestAST.test(input,expect,401))

    def test_AssignWithArraycell(self):
        input = """
            procedure main();
            begin
                a := 2[2];
            end
            """
        expect = str(Program([FuncDecl(Id("main"),
                                       [],
                                       [],
                                       [Assign(Id("a"),
                                               ArrayCell(IntLiteral(2),IntLiteral(2)))]
                                      )
                             ]
                            )
                    )
        self.assertTrue(TestAST.test(input,expect,402))
