import React from "react"
import MetaTags from 'react-meta-tags';
import { Link } from "react-router-dom"
import { Container, Row, Col } from "reactstrap"

//Import Countdown
import Countdown from "react-countdown"

//Import Images
import maintanence from "../assets/images/coming-soon.svg"

const PagesComingsoon = () => {
  const renderer = ({ days, hours, minutes, seconds, completed }) => {
    if (completed) {
      // Render a completed state
      return <span>You are good to go!</span>
    } else {
      return (
        <>
          <div className="coming-box">
            {days} <span>Days</span>
          </div>{" "}
          <div className="coming-box">
            {hours} <span>Hours</span>
          </div>{" "}
          <div className="coming-box">
            {minutes} <span>Minutes</span>
          </div>{" "}
          <div className="coming-box">
            {seconds} <span>Seconds</span>
          </div>
        </>
      )
    }
  }

  return (
    <React.Fragment>
      <MetaTags>
        <title>Em construção!</title>
      </MetaTags>

      <div className="my-5 pt-sm-5">
        <Container>
          <Row>
            <Col lg="12">
              <div className="text-center">
                <Row className="justify-content-center mt-5">
                  <Col sm="4">
                    <div className="maintenance-img">
                      <img
                        src={maintanence}
                        alt=""
                        className="img-fluid mx-auto d-block"
                      />
                    </div>
                  </Col>
                </Row>
                <h4 className="mt-5">Em construção!</h4>
                
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    </React.Fragment>
  )
}

export default PagesComingsoon
