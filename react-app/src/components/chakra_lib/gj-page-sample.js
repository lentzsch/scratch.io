import React, { useEffect, useState} from "react";
import { useSelector, useDispatch } from "react-redux";
import { getGameJams } from "../../store/game_jam"
import { gameJamQuery } from "../../utils/queryFunctions"

import GJInfoBox from "../GJInfoBox";


import {Box, Flex, Input, InputGroup, IconButton, InputRightElement, Select, Grid} from "@chakra-ui/react"
import { SearchIcon } from "@chakra-ui/icons"
import CardSample2 from "./card-sample-2";
import MainCarousel from "./mainCarousel";
import BigMainCarousel from "./bigMainCarousel";
import FloatinCardSimple from "./floatin-card-simple";
import Carousel from "./carousel";


export default function GameJamPageSample() {
    const dispatch = useDispatch()
    const gameJams = useSelector(state => state.gameJams)

    const [searchTerm, setSearchTerm] = useState("")
    const [date, setDate] = useState("")


    useEffect(() => {

        dispatch(getGameJams(gameJamQuery()))

    }, [dispatch])

    const handleClick = (e) => {
        e.preventDefault()

        dispatch(getGameJams(gameJamQuery({searchTerm: searchTerm, date: date})))
    }

    return (
        <>
        <Flex>
            <Box w="100%" h="200px" bgColor="black">
                <Flex direction="column">
                    <Box>
                        <InputGroup size="md" w="60%">
                            <Input
                                placeholder="Search"
                                variant="outline"
                                onChange={(e) => setSearchTerm(e.target.value)}
                            />
                            <InputRightElement>
                                    <IconButton aria-label="Search database" icon={<SearchIcon />}  onClick={handleClick}/>
                            </InputRightElement>
                        </InputGroup>
                        <Select placeholder="Select Date" bgColor="gray.200" w="15%" onChange={(e) => setDate(e.target.value)}>
                            <option value="day">Next Day</option>
                            <option value="week">Next Week</option>
                            <option value="month">Next Month</option>
                            <option value="year">Next Year</option>
                            <option value="all">All Game Jams</option>
                        </Select>
                    </Box>
                </Flex>
            </Box>
        </Flex>
        <Grid templateRows="repeat(2, 1fr)" gap={6}>
            <Box>
                <CardSample2 gameJams={gameJams} />
            </Box>
        </Grid>
    </>
    )
}
