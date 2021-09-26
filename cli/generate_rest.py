#!/usr/bin/env python

from gotypes import types, imports

res = "// Code generated by generate_rest.py; DO NOT EDIT.\n"
res += "\n"
res += "package cli\n"
res += "\n"
res += "import (\n"
for pkg in imports:
    res += "\t\"%s\"\n" % pkg
res += ")\n"

for (typ, name, _, _) in types:
    res += "\n"
    res += "// []%s\n" % typ
    res += "\n"
    res += "// Rest%ssVar defines the []%s rest arguments with specified name.\n" % (name, typ)
    res += "// The argument p points to a []%s variable in which to store values of arguments.\n" % typ
    res += "// The return value will be an error from the register.RegisterRestArgs if it\n"
    res += "// failed to register the rest arguments.\n"
    res += "//\n"
    res += "// A usage may be set by passing a cli.Usage.\n"
    res += "//\n"
    res += "//   _ = cli.Rest%ssVar(register, &p, \"names\", cli.Usage(\"Names of users\"))\n" % name
    # res += "//\n"
    # res += "// All options can be used together.\n"
    res += "func Rest%ssVar(register Register, p *[]%s, name string, options ...RestOptionApplyer) error {\n" % (name, typ)
    res += "\treturn RestVar(register, new%sValues(p), name, options...)\n" % name
    res += "}\n"
    res += "\n"
    res += "// Rest%ss defines the []%s rest arguments with specified name.\n" % (name, typ)
    res += "// The return value is the address of a []%s variable that stores values of arguments.\n" % typ
    res += "//\n"
    res += "// A usage may be set by passing a cli.Usage.\n"
    res += "//\n"
    res += "//   _ = cli.Rest%ss(register, \"names\", cli.Usage(\"Names of users\"))\n" % name
    # res += "//\n"
    # res += "// All options can be used together.\n"
    res += "func Rest%ss(register Register, name string, options ...RestOptionApplyer) *[]%s {\n" % (name, typ)
    res += "\tp := new([]%s)\n" % typ
    res += "\t_ = Rest%ssVar(register, p, name, options...)\n" % name
    res += "\treturn p\n"
    res += "}\n"

with open("./rest_gen.go", "w") as f:
    f.write(res)
