import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Th, Td } from "react-super-responsive-table";
import "react-super-responsive-table/dist/SuperResponsiveTableStyle.css";
import Loading from "components/CommonForBoth/Loading";

class GreekTable extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        //Componente correto
        let tableContent;
        let loading = <Loading />;
        if (this.props.data != null) {
            tableContent = <Table
                id="greeks"
                className="table table-striped table-bordered"
            >
                <Thead>
                    <Tr>
                        <Th>Greeks</Th>
                        {this.props.data.map((e, index) => (
                            <Th key={index}>{e.name}</Th>
                        ))}
                    </Tr>
                </Thead>
                <Tbody>
                    <Tr>
                        <Td>Valores</Td>
                        {this.props.data.map((e, index) => (
                            <Th key={index}>{e.value}</Th>
                        ))}
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
                                <h4 className="card-title mb-4">{this.props.id}</h4>
                            </div>
                            <Row>
                                <Col lg="12">
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

GreekTable.propTypes = {
    data: PropTypes.array,
    id: PropTypes.string
}

export default GreekTable;