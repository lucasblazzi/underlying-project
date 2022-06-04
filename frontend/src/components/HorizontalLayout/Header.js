import React, { useState } from "react"
import PropTypes from 'prop-types'
import ReactDrawer from 'react-drawer';
import 'react-drawer/lib/react-drawer.css';

import { connect } from "react-redux"

import { Link } from "react-router-dom"

// Redux Store
import { toggleLeftmenu } from "../../store/actions"
// reactstrap
import { Row, Col, Dropdown, DropdownToggle, DropdownMenu } from "reactstrap"

// Import menuDropdown
import ProfileMenu from "../CommonForBoth/TopbarDropdown/ProfileMenu"

import logo from "../../assets/images/logo.svg"
import logoLight from "../../assets/images/logo-light.png"
import logoLightSvg from "../../assets/images/logo-light.svg"
import logoDark from "../../assets/images/logo-dark.png"
import logoUnderlying from "../../assets/images/logo-underlying-light.png"

//i18n
import { withTranslation } from "react-i18next"

const Header = props => {
  const [menu, setMenu] = useState(false)
  const [isSearch, setSearch] = useState(false)
  const [socialDrp, setsocialDrp] = useState(false)
  const [position, setPosition] = useState();
  const [open, setOpen] = useState(false);

  const toggleTopDrawer = () => {
    setPosition('right');
    setOpen(!open)
  }

  const onDrawerClose = () => {
    setOpen(false);
  }

  function toggleFullscreen() {
    if (
      !document.fullscreenElement &&
      /* alternative standard method */ !document.mozFullScreenElement &&
      !document.webkitFullscreenElement
    ) {
      // current working methods
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen()
      } else if (document.documentElement.mozRequestFullScreen) {
        document.documentElement.mozRequestFullScreen()
      } else if (document.documentElement.webkitRequestFullscreen) {
        document.documentElement.webkitRequestFullscreen(
          Element.ALLOW_KEYBOARD_INPUT
        )
      }
    } else {
      if (document.cancelFullScreen) {
        document.cancelFullScreen()
      } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen()
      } else if (document.webkitCancelFullScreen) {
        document.webkitCancelFullScreen()
      }
    }
  }
  return (
    <React.Fragment>
      <header id="page-topbar">
        <div className="navbar-header">
          <div className="d-flex">
            <div className="navbar-brand-box">
              <Link to="/search" className="logo logo-dark">
                <span className="logo-sm">
                  <img src={logoUnderlying} alt="" height="22" />
                </span>
                <span className="logo-lg">
                  <img src={logoUnderlying} alt="" height="17" />
                </span>
              </Link>

              <Link to="/search" className="logo logo-light">
                <span className="logo-sm">
                  <img src={logoUnderlying} alt="" height="22" />
                </span>
                <span className="logo-lg">
                  <img src={logoUnderlying} alt="" height="50" width="250"/>
                </span>
              </Link>
            </div>

          </div>

          <div className="d-flex">
            <div className="dropdown d-inline-block d-lg-none ms-2">
              
              
            </div>


            {<Dropdown
              className="d-none d-lg-inline-block ms-1"
              isOpen={socialDrp}
              toggle={() => {
                setsocialDrp(!socialDrp)
              }}
            >
              
            </Dropdown>}

            <div className="dropdown d-none d-lg-inline-block ms-1">
              <button
                type="button"
                className="btn header-item noti-icon "
                onClick={() => {
                  toggleFullscreen()
                }}
                data-toggle="fullscreen"
              >
                <i className="bx bx-fullscreen" />
              </button>
            </div>

            <ProfileMenu />

          </div>
        </div>
      </header>
      <ReactDrawer
        open={open}
        position={position}
        onClose={onDrawerClose}
      >

      </ReactDrawer>
    </React.Fragment>
  )
}

Header.propTypes = {
  leftMenu: PropTypes.any,
  t: PropTypes.any,
  toggleLeftmenu: PropTypes.func
}

const mapStatetoProps = state => {
  const { layoutType, leftMenu } = state.Layout
  return { layoutType, leftMenu }
}

export default connect(mapStatetoProps, {
  toggleLeftmenu,
})(withTranslation()(Header))
