--- Select useful data for our analysis 
Select location, date, total_cases, new_cases, total_deaths, population
FROM PortflolioProject..CovidDeaths$
order by 1,2

-- Looking at total cases vs total deaths ( case of Cameroun)
-- How likely are you to die if you contract COVID
Select location,date, total_cases,  total_deaths, 100*(total_deaths/total_cases) as  pct_dead
From PortflolioProject..CovidDeaths$
Where location like '%Cameroon%'
order by 1,2

-- Total cases vs the population
--Percentage of the population that has been infected with CoVid
Select location,date, population, total_cases, 100*(total_cases/population) as  pct_case
From PortflolioProject..CovidDeaths$
Where location like '%Cameroon%'
order by 1,2

--Country with the highest infection rate
Select location, population, max(total_cases) as highestInfectionCount,
       max(100*(total_cases/population)) as  highest_pct_case
From PortflolioProject..CovidDeaths$
GROUP BY location,population
order by highest_pct_case DESC

-- Countries with the highest death rate
Select location, MAX(CAST(total_deaths AS int)) as TotalDeathCount
From PortflolioProject..CovidDeaths$
Where continent is not null
GROUP BY location
order by TotalDeathCount DESC

-- we notice in our location column we have regroupment such as World, Europe, Asia, etc Hence the where statement

--Breakdown of the countries with the highest death rate by continent
Select location, MAX(CAST(total_deaths AS int)) as TotalDeathCount
From PortflolioProject..CovidDeaths$
Where continent is null And location <> 'World'
GROUP BY location
order by TotalDeathCount DESC

--Death counts per continient 
Select location,date, total_cases,  total_deaths, 100*(total_deaths/total_cases) as  pct_dead
From PortflolioProject..CovidDeaths$
Where continent is null And location <> 'World'
order by 1,2

Select date, sum(new_cases)as total_cases, SUM(cast(new_deaths as int)) as total_deaths, 100*SUM(cast(new_deaths as int))/(1+SUM(New_cases ))as pct_death
From PortflolioProject..CovidDeaths$
Where continent is null And location <> 'World'
Group by date
order by 1,2

--Baseline rate for the whole world of death counts 
Select  sum(new_cases)as total_cases, SUM(cast(new_deaths as int)) as total_deaths, 100*SUM(cast(new_deaths as int))/(1+SUM(New_cases ))as pct_death
From PortflolioProject..CovidDeaths$
Where continent is null And location <> 'World'
--Group by date
order by 1,2

-- Total Population vs Vaccinations
Select deaths.continent, deaths.location, deaths.date, deaths.population,vacc.new_vaccinations
From PortflolioProject..CovidVaccinations$ vacc
JOIN PortflolioProject..CovidDeaths$ deaths
	On deaths.location = vacc.location
	and deaths.date = vacc.date
Where deaths.continent is not null
order by 2,3

--Rolling count of vaccinations
Select deaths.continent, deaths.location, deaths.date, deaths.population,vacc.new_vaccinations,
SUM(cast(vacc.new_vaccinations as int)) OVER (Partition by deaths.location Order by deaths.location, deaths.date) as RollingPeopleVacc,

From PortflolioProject..CovidVaccinations$ vacc
JOIN PortflolioProject..CovidDeaths$ deaths
	On deaths.location = vacc.location
	and deaths.date = vacc.date
Where deaths.continent is not null
order by 2,3

--CTE 
WITH PopvsVac(continent,location,date,population,new_vaccinations, RollingPeopleVaccinated) 
as
(
Select deaths.continent, deaths.location, deaths.date, deaths.population,vacc.new_vaccinations,
SUM(cast(vacc.new_vaccinations as int)) OVER (Partition by deaths.location Order by deaths.location, deaths.date) as RollingPeopleVacc
From PortflolioProject..CovidVaccinations$ vacc
JOIN PortflolioProject..CovidDeaths$ deaths
	On deaths.location = vacc.location
	and deaths.date = vacc.date
Where deaths.continent is not null
--order by 2,3
)

Select * ,100*(RollingPeopleVaccinated/population) as pct_rolling_vacc
From PopvsVac

--TEMP TABLE 
SET ANSI_WARNINGS OFF
GO
Drop Table if exists #PercentPopulationVaccins
Create Table #PercentPopulationVaccins
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime ,
Population numeric,
New_vaccinations numeric, 
RollingPeopleVaccinated numeric
)
Insert into #PercentPopulationVaccins
Select deaths.continent, deaths.location, deaths.date, deaths.population,vacc.new_vaccinations,
SUM(CONVERT(int,vacc.new_vaccinations)) OVER (Partition by deaths.location Order by deaths.location, deaths.date) as RollingPeopleVacc
From PortflolioProject..CovidVaccinations$ vacc
JOIN PortflolioProject..CovidDeaths$ deaths
	On deaths.location = vacc.location
	and deaths.date = vacc.date
Where deaths.continent is not null
order by 2,3

--Create a view
Create View PercentPopulationVaccinated as 
Select deaths.continent, deaths.location, deaths.date, deaths.population,vacc.new_vaccinations,
SUM(cast(vacc.new_vaccinations as int)) OVER (Partition by deaths.location Order by deaths.location, deaths.date) as RollingPeopleVacc
From PortflolioProject..CovidVaccinations$ vacc
JOIN PortflolioProject..CovidDeaths$ deaths
	On deaths.location = vacc.location
	and deaths.date = vacc.date
Where deaths.continent is not null
--order by 2,3