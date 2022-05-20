import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Th, Td } from "react-super-responsive-table";
import "react-super-responsive-table/dist/SuperResponsiveTableStyle.css";
import Loading from "components/CommonForBoth/Loading";

class PriceTable extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        //Componente correto
        let tableRows;
        let loading = <Loading />;
        if (this.props.data != null) {
            tableRows = <Table
                id="price"
                className="table table-striped table-bordered"
            >
                <Thead>
                    <Tr>
                        <Th></Th>
                        <Th>Open price</Th>
                        <Th>Max price</Th>
                        <Th>Min price</Th>
                        <Th>Average price</Th>
                        <Th>Close price</Th>
                        <Th>Best buy price</Th>
                        <Th>Best sell price</Th>
                        <Th>Transactions</Th>
                        <Th>Quantity</Th>
                        <Th>Volume</Th>
                    </Tr>
                </Thead>
                <Tbody>
                    <Tr>
                        <Td>Valor</Td>
                        {this.props.data.map((e, index) => (
                            <Td key={index}>{e.value}</Td>

                        ))}

                    </Tr>
                </Tbody>
            </Table>
        }

        //Condicional que irá renderizar
        let propsData = this.props.data == null ? loading : tableRows
        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <div className="clearfix">
                                <h4 className="card-title mb-4">Tabela de preços</h4>
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

PriceTable.propTypes = {
    data: PropTypes.array,
}

export default PriceTable;