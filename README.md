# TrafficTesting
Simple Python Web App for load testing


---

Commands for building the solution in .NET

Building the Web API

```sh
$ dotnet new webapi --use-controllers -o [Name]
```

Installing dependencies
```sh
$ dotnet add package Microsoft.EntityFrameworkCore.Sqlite
$ dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
# $ dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
$ dotnet add package Microsoft.EntityFrameworkCore.Design
$ dotnet add package Microsoft.EntityFrameworkCore.SqlServer
$ dotnet add package Microsoft.EntityFrameworkCore.Tools
```

Autogen for API Controller
```sh
$ dotnet aspnet-codegenerator controller -name [ControllerName] -async -api -m [ModelName] -dc [DbContextName] -outDir [OutputDir]
```

1. Configuration of EF Core
```sh
$ dotnet ef migrations add [Name]
$ dotnet ef database update 
```

2. Building and running the Web API
```sh
$ dotnet build
$ dotnet run
```

Cleaning the build executable
```sh
$ dotnet clean
```

