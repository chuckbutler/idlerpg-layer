#!/bin/bash

mkdir -p $CHARM_DIR/data
mkdir -p $CHARM_DIR/backups
cp $CHARM_DIR/files/events.txt $CHARM_DIR/data/events.txt
cp $CHARM_DIR/files/irpg.db $CHARM_DIR/data/irpg.db
