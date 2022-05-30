import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Th, Td } from "react-super-responsive-table";
import ReactApexChart from "react-apexcharts";

class OptsShortChart extends Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {
        var series = [
            {
                name: "Lucro / Prejuízo",
                data: this.props.data.y,
            },
        ];
        var options = {
            chart: {
                toolbar: "false",
            },
            dataLabels: {
                enabled: !1,
            },
            labels: this.props.data.x,
            colors: ["#25526E"],
            stroke: {
                curve: "smooth",
                width: 3,
            },
        };

        let tableContent;

        if (this.props.data != null) {
            tableContent = <Table
                id="short"
                className="table table-striped table-bordered"
            >
                <Thead>
                    <Tr>
                        
                    </Tr>
                </Thead>
                <Tbody>
                    <Tr>
                        <Td>Preço de exercício</Td>
                        <Td>{this.props.data.exercise_price}</Td>
                    </Tr>
                    <Tr>
                        <Td>Nome</Td>
                        <Td>{this.props.data.name}</Td>
                    </Tr>
                    <Tr>
                        <Td>Preço de fechamento</Td>
                        <Td>{this.props.data.close_price}</Td>
                    </Tr>
                    <Tr>
                        <Td>Número de papéis</Td>
                        <Td>{this.props.data.contracts}</Td>
                    </Tr>
                    <Tr>
                        <Td>Tipo da opção</Td>
                        <Td>{this.props.data.type}</Td>
                    </Tr>
                    <Tr>
                        <Td>Tipo da transação</Td>
                        <Td>{this.props.data.transaction_type}</Td>
                    </Tr>
                </Tbody>
            </Table>
        }

        //Condicional que irá renderizar
        let propsData = this.props.data == null ? loading : tableContent

        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <div className="clearfix">
                                <h4 className="card-title mb-4">Payoff Short</h4>
                            </div>
                            <Row>
                                <Col lg="8">
                                    <div id="line-chart" className="apex-charts" dir="ltr">
                                        <ReactApexChart
                                            series={series}
                                            options={options}
                                            type="line"
                                            height={320}
                                            className="apex-charts"
                                        />
                                    </div>
                                </Col>
                                <Col lg="4">
                                    <div className="table-rep-plugin">
                                        <div
                                            className="table-responsive mb-0"
                                            data-pattern="priority-columns"
                                        >
                                            {propsData}
                                        </div>
                                    </div>
                                </Col>
                            </Row>
                        </CardBody>
                    </Card>
                </Col>
            </>
        );
    }
}

OptsShortChart.propTypes = {
    data: PropTypes.object,
}

export default OptsShortChart;