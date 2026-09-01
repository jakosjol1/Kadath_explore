-- Kadath_explore initial schema
-- Applied to Supabase project: kadath-explore (dfuqhspmstqcrurtdutu, eu-north-1)
-- Applied 2026-09-01 via Supabase MCP `apply_migration`.

-- Reference table: which macro series we track
create table macro_series (
    series_id text primary key,
    description text,
    unit text,
    source text default 'kadath'
);

-- Raw macro observations, PIT-safe (as_of preserved for traceability)
create table macro_observations (
    series_id text not null references macro_series(series_id),
    obs_date date not null,
    value numeric not null,
    as_of date not null,
    inserted_at timestamptz not null default now(),
    primary key (series_id, obs_date)
);

-- Reference table: portfolios we track, including a synthetic 'MARKET' row
-- to represent benchmark-level (OMXSPI) comparison, so macro-vs-market and
-- macro-vs-portfolio share the same downstream schema.
create table portfolios (
    portfolio_id text primary key,
    description text,
    rebal_freq text,
    w_max numeric,
    benchmark text,
    is_synthetic_market boolean not null default false
);

-- NAV time series per portfolio, from l9_get_nav_history
create table portfolio_nav_history (
    portfolio_id text not null references portfolios(portfolio_id),
    rebal_date date not null,
    execution_date date,
    nav numeric,
    gross_return_pct numeric,
    commission numeric,
    position_count int,
    as_of date not null,
    inserted_at timestamptz not null default now(),
    primary key (portfolio_id, rebal_date)
);

-- Per-period attribution breakdown, from l10_get_period_returns
create table portfolio_period_returns (
    portfolio_id text not null references portfolios(portfolio_id),
    period_start date not null,
    period_end date not null,
    gross_return_pct numeric,
    benchmark_return_pct numeric,
    active_return_pct numeric,
    factor_return_pct numeric,
    specific_return_pct numeric,
    as_of date not null,
    inserted_at timestamptz not null default now(),
    primary key (portfolio_id, period_end)
);

create index idx_macro_obs_date on macro_observations(obs_date);
create index idx_nav_rebal_date on portfolio_nav_history(rebal_date);
create index idx_period_returns_end on portfolio_period_returns(period_end);


-- ============================================================
-- Migration 002: seed reference data + synthetic MARKET row
-- Applied 2026-09-01 via Supabase MCP `apply_migration`.
-- ============================================================

insert into macro_series (series_id, description, unit, source) values
    ('vix', 'CBOE Volatility Index', 'index', 'kadath'),
    ('us_10y', 'US 10-Year Treasury Yield', 'percent', 'kadath'),
    ('se_policy', 'Riksbank policy rate', 'percent', 'kadath')
on conflict (series_id) do nothing;

-- Synthetic MARKET row so macro-vs-market comparisons share the same
-- downstream tables as macro-vs-portfolio comparisons.
insert into portfolios (portfolio_id, description, rebal_freq, w_max, benchmark, is_synthetic_market) values
    ('MARKET', 'Synthetic row representing OMXSPI benchmark-level comparison (not an actual portfolio)', null, null, 'OMXSPI', true)
on conflict (portfolio_id) do nothing;

-- Real portfolio reference rows (from l8_get_portfolios, live 2026-09-01)
insert into portfolios (portfolio_id, description, rebal_freq, w_max, benchmark, is_synthetic_market) values
    ('mvl8_largecap_v1', 'Concentrated monthly portfolio; GK-scaled alphas, Barra ff_v1, SE mkt cap >= 10B SEK', 'monthly', 0.15, 'OMXSPI', false),
    ('mvl8_monthly_v1', 'Monthly mean-variance portfolio; GK-scaled alphas, Barra ff_v1, equal-weight benchmark proxy', 'monthly', 0.05, 'OMXSPI', false),
    ('mvl8_quarterly_v1', 'Quarterly mean-variance portfolio; 63-day GK horizon', 'quarterly', 0.05, 'OMXSPI', false),
    ('mvl8_semiannual_v1', 'Semi-annual mean-variance portfolio; 126-day GK horizon', 'semiannual', 0.05, 'OMXSPI', false)
on conflict (portfolio_id) do nothing;

-- NOTE: macro_observations for Aug 2026 (vix, us_10y, se_policy) were
-- backfilled manually via a Claude chat session (live Kadath MCP
-- connection) rather than the standalone sync script, since that script
-- is still blocked on a Kadath API credential. See sync/kadath_to_supabase.py
-- docstring. Not included here as raw INSERTs -- re-run the same manual
-- process or the script (once credentialed) to reproduce.
