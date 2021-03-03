FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ./services/tecan-spark-relay/TecanSparkRelay.csproj ./
RUN dotnet restore ./TecanSparkRelay.csproj

COPY ./services/tecan-spark-relay ./
ENTRYPOINT ["dotnet", "run"]
