"""
Created on Sept 12 2016

@author: Derek
"""
from bi_etl.components.readonlytable import ReadOnlyTable
from bi_etl.scheduler.task import ETLTask
from bi_etl.database.database_metadata import DatabaseMetadata


class CopyTableData(ETLTask):
    def depends_on(self):
        return []

    def load(self):
        datbase_entry = self.get_parameter('datbase_entry')
        if isinstance(datbase_entry, DatabaseMetadata):
            database = datbase_entry
        else:
            database = self.get_database(self.get_parameter('datbase_entry'))
        source_table_name = self.get_parameter('source_table')
        target_table_name = self.get_parameter('target_table')

        with ReadOnlyTable(
                self,
                database,
                source_table_name,
                table_name_case_sensitive=True,
                ) as source_data:
            with ReadOnlyTable(
                    self,
                    database,
                    target_table_name,
                    table_name_case_sensitive=True,
                    ) as target_tbl:
                target_column_set = set(target_tbl.column_names)
                common_columns = list()
                for source_col in source_data.column_names:
                    if source_col in target_column_set:
                        common_columns.append(source_col)

                cols = ""
                sep = ""
                for column in common_columns:
                    cols += sep
                    cols += column
                    sep = ","

                sql = "INSERT INTO {target_table_name} ({cols})"\
                      "SELECT {cols} FROM {source_table_name}"\
                      .format(
                         source_table_name=source_table_name,
                         target_table_name=target_table_name,
                         cols=cols)

                self.log.debug(sql)

                database.execute(sql, transaction=True)

        self.log.info("Done")
