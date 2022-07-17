import React from "react"
import { Redirect } from "react-router-dom"

// Profile
import UserProfile from "../pages/Authentication/user-profile"

// Authentication related pages
import Login from "../pages/Authentication/Login"
import Logout from "../pages/Authentication/Logout"
import Register from "../pages/Authentication/Register"
import ForgetPwd from "../pages/Authentication/ForgetPassword"

// Dashboard
import Dashboard from "../pages/Dashboard/index"
import newPage from "pages/newPage"
import duvidas from "pages/duvidas"
import Pages404 from "pages/pages-404"
import Opts from "pages/Opts"
import Search from "pages/Search"
import PagesComingsoon from "components/pages-comingsoon"
import Strategies from "pages/Strategies"
import Glossary from "pages/Glossary"
import SharedStrategies from "pages/Strategies/shared"
import ViewStrategy from "pages/Strategies/view"
import PersonalStrategies from "pages/Strategies/personal"

const authProtectedRoutes = [
  { path: "/dashboard", component: Search },

  // //profile
  { path: "/profile", component: UserProfile },

  //Nova página
  { path: "/new-page", component: newPage },
  { path: "/duvidas", component: duvidas },

  { path: "/opts", component: Opts },

  { path: "/search", component: Search },

  { path: "/strategies", component: Strategies },
  { path: "/view-strategies", component: SharedStrategies },
  { path: "/view-strategy", component: ViewStrategy },
  { path: "/my-strategies", component: PersonalStrategies },

  { path: "/glossary", component: Glossary },

  { path:"/coming-soon", component: PagesComingsoon},
  { path: "/", component: Search },

  // this route should be at the end of all other routes
  // eslint-disable-next-line react/display-name
  { path: "*", exact: true, component: () => <Redirect to="/not-found" /> },
]

const publicRoutes = [
  { path: "/logout", component: Logout },
  { path: "/login", component: Login },
  { path: "/forgot-password", component: ForgetPwd },
  { path: "/register", component: Register },
  
  //Página 404
  { path:"/not-found", component: Pages404 },
]

export { publicRoutes, authProtectedRoutes }
