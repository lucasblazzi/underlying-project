import React from 'react';
import ViewStrategy from '../../pages/Strategies/view';
import renderer from 'react-test-renderer';
import SearchBar from "../../pages/Opts/OptsShortChart";

it('Página', () => {
    const tree = renderer.create(<div class = "page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<div class="m-3" />).toJSON();
    expect(tree).toMatchSnapshot();
})